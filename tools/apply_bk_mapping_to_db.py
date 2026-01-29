"""Apply Brikick mapping (bk_mapping.csv) into the final SQLite DB.

Requirements (per request)
-------------------------
- A CSV (bk_mapping.csv) must be used to map each bl_part_id -> bk_part_id.
- Also persist: item_type, brikick_name, api_item_type, bk_part_key.
- Do NOT modify existing upstream pipeline code.

Implementation
--------------
- Create/refresh a separate table `bk_mapping` in the same DB.
- Update `brickovery_db.bk_part_id` from this mapping (no schema changes).

This is safe with brickovery_upstream_v3.py because that script will only
rebuild the `brickovery_db` table when its *columns* differ; it does not drop
additional tables.
"""

from __future__ import annotations

import argparse
import csv
import sqlite3
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple


def _norm(s: Optional[str]) -> str:
    return (s or "").strip()


def _lower(s: Optional[str]) -> str:
    return _norm(s).lower()


def _canon_item_type(it: Optional[str]) -> str:
    # Keep identical semantics to existing pipeline (P default)
    it = _lower(it)
    if not it:
        return "P"
    if it in ("part", "parts"):
        return "P"
    return it.upper()


def _detect_cols(fieldnames: Iterable[str]) -> Dict[str, str]:
    """Return mapping of required logical fields -> actual CSV column names."""
    fn = {f.strip(): f for f in fieldnames if f is not None}
    lmap = {f.lower().strip(): f for f in fieldnames if f is not None}

    def pick(*cands: str) -> Optional[str]:
        for c in cands:
            if c in fn:
                return fn[c]
            if c.lower() in lmap:
                return lmap[c.lower()]
        return None

    col_bl = pick("bl_part_id", "bl_part", "bricklink_part_id", "bl_id")
    col_bk = pick("bk_part_id", "brikick_part_id", "bk_id")
    col_it = pick("item_type", "bl_item_type", "type")
    col_name = pick("brikick_name", "bk_name", "name")
    col_api_it = pick("api_item_type", "api_type")
    col_key = pick("bk_part_key", "bk_key", "part_key")

    missing = [
        ("bl_part_id", col_bl),
        ("bk_part_id", col_bk),
    ]
    hard_missing = [k for k, v in missing if not v]
    if hard_missing:
        raise ValueError(
            f"CSV não tem colunas obrigatórias: {', '.join(hard_missing)}. "
            f"Encontradas: {list(fieldnames)}"
        )

    return {
        "bl_part_id": col_bl,
        "bk_part_id": col_bk,
        "item_type": col_it or "",
        "brikick_name": col_name or "",
        "api_item_type": col_api_it or "",
        "bk_part_key": col_key or "",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True, help="Path to database/brickovery.db")
    ap.add_argument("--mapping-csv", required=True, help="Path to bk_mapping.csv")
    args = ap.parse_args()

    db_path = Path(args.db)
    csv_path = Path(args.mapping_csv)
    if not db_path.exists():
        raise FileNotFoundError(f"DB não encontrada: {db_path}")
    if not csv_path.exists():
        raise FileNotFoundError(f"bk_mapping.csv não encontrado: {csv_path}")

    con = sqlite3.connect(str(db_path))
    cur = con.cursor()
    try:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS bk_mapping(
              bl_part_id   TEXT NOT NULL,
              item_type    TEXT,
              bk_part_id   TEXT,
              brikick_name TEXT,
              api_item_type TEXT,
              bk_part_key  TEXT,
              updated_at   INTEGER NOT NULL,
              PRIMARY KEY (bl_part_id, item_type)
            )
            """
        )

        now = int(__import__("time").time())

        with open(csv_path, "r", encoding="utf-8", newline="") as f:
            rdr = csv.DictReader(f)
            if not rdr.fieldnames:
                raise ValueError("CSV sem header")
            cols = _detect_cols(rdr.fieldnames)

            rows = []
            for r in rdr:
                bl = _norm(r.get(cols["bl_part_id"]))
                bk = _norm(r.get(cols["bk_part_id"]))
                if not bl:
                    continue
                it = _canon_item_type(r.get(cols["item_type"])) if cols["item_type"] else ""
                name = _norm(r.get(cols["brikick_name"])) if cols["brikick_name"] else ""
                api_it = _norm(r.get(cols["api_item_type"])) if cols["api_item_type"] else ""
                key = _norm(r.get(cols["bk_part_key"])) if cols["bk_part_key"] else ""
                rows.append((bl, it, bk, name, api_it, key, now))

        # Upsert mapping rows
        cur.executemany(
            """
            INSERT INTO bk_mapping(
              bl_part_id,item_type,bk_part_id,brikick_name,api_item_type,bk_part_key,updated_at
            ) VALUES (?,?,?,?,?,?,?)
            ON CONFLICT(bl_part_id,item_type) DO UPDATE SET
              bk_part_id=excluded.bk_part_id,
              brikick_name=excluded.brikick_name,
              api_item_type=excluded.api_item_type,
              bk_part_key=excluded.bk_part_key,
              updated_at=excluded.updated_at
            """,
            rows,
        )

        # Update brickovery_db.bk_part_id (two passes: specific item_type then generic)
        cur.execute(
            """
            UPDATE brickovery_db
               SET bk_part_id = (
                 SELECT m.bk_part_id
                   FROM bk_mapping m
                  WHERE m.bl_part_id = brickovery_db.bl_part_id
                    AND m.item_type = brickovery_db.item_type
                    AND m.bk_part_id IS NOT NULL AND m.bk_part_id != ''
                  LIMIT 1
               )
             WHERE EXISTS(
                 SELECT 1 FROM bk_mapping m
                  WHERE m.bl_part_id = brickovery_db.bl_part_id
                    AND m.item_type = brickovery_db.item_type
                    AND m.bk_part_id IS NOT NULL AND m.bk_part_id != ''
             )
            """
        )

        # Generic mapping rows use item_type == ''
        cur.execute(
            """
            UPDATE brickovery_db
               SET bk_part_id = (
                 SELECT m.bk_part_id
                   FROM bk_mapping m
                  WHERE m.bl_part_id = brickovery_db.bl_part_id
                    AND (m.item_type IS NULL OR m.item_type = '')
                    AND m.bk_part_id IS NOT NULL AND m.bk_part_id != ''
                  LIMIT 1
               )
             WHERE (bk_part_id IS NULL OR bk_part_id = '')
               AND EXISTS(
                 SELECT 1 FROM bk_mapping m
                  WHERE m.bl_part_id = brickovery_db.bl_part_id
                    AND (m.item_type IS NULL OR m.item_type = '')
                    AND m.bk_part_id IS NOT NULL AND m.bk_part_id != ''
               )
            """
        )

        con.commit()
        print(
            f"bk_mapping rows upserted: {len(rows)}; brickovery_db updated bk_part_id rows: {con.total_changes}"
        )
        return 0
    finally:
        con.close()


if __name__ == "__main__":
    raise SystemExit(main())
