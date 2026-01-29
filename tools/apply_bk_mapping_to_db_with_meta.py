#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apply/ensure BK mapping into the final SQLite DB.

Goal:
- Ensure brickovery_db table contains (and is populated with):
  bl_part_id, bk_part_id, item_type, brikick_name, api_item_type, bk_part_key

Behavior:
- Loads bk_mapping.csv (must contain at least the columns above; extra columns are tolerated).
- For any (bl_part_id,item_type) present in DB and missing in CSV:
    * auto-generates a new BK id/key using per-item_type counters (no collisions),
    * appends the new row to bk_mapping.csv (optional),
    * updates brickovery_db columns for all colors for that (bl_part_id,item_type).
- Also maintains an internal table bk_mapping (optional but useful) inside the same DB.

This script is designed to run *after* brickovery_upstream_v3.py builds/updates the DB.
"""

from __future__ import annotations

import argparse
import csv
import re
import sqlite3
from pathlib import Path
from typing import Dict, Iterable, List, Tuple, Optional

BK_KEY_RE = re.compile(r"^BK-([A-Z])-([0-9]{8})$")

TYPE_META = {
    "P": ("Parts", "PART"),
    "S": ("Sets", "SET"),
    "M": ("Minifigures", "MINIFIG"),
    "B": ("Books", "BOOK"),
    "G": ("Gear", "GEAR"),
    "C": ("Catalogs", "CATALOG"),
    "I": ("Instructions", "INSTRUCTION"),
    "O": ("Original Boxes", "ORIGINAL_BOX"),
    "U": ("Unsorted Lots", "UNSORTED_LOT"),
}


def _cols(con: sqlite3.Connection, table: str) -> Dict[str, str]:
    cur = con.cursor()
    out: Dict[str, str] = {}
    for cid, name, ctype, notnull, dflt, pk in cur.execute(f'PRAGMA table_info("{table}")'):
        out[name] = ctype or "TEXT"
    return out


def _ensure_columns(con: sqlite3.Connection) -> None:
    cur = con.cursor()
    cols = _cols(con, "brickovery_db")
    # These columns must exist for "incorporadas dentro da db final"
    need = {
        "brikick_name": "TEXT",
        "api_item_type": "TEXT",
        "bk_part_key": "TEXT",
    }
    for c, ctype in need.items():
        if c not in cols:
            cur.execute(f'ALTER TABLE brickovery_db ADD COLUMN {c} {ctype}')
    con.commit()

    # Optional internal mapping table (simple and stable)
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS bk_mapping (
          bl_part_id TEXT NOT NULL,
          item_type TEXT NOT NULL,
          bk_part_id TEXT NOT NULL,
          brikick_name TEXT,
          api_item_type TEXT,
          bk_part_key TEXT,
          PRIMARY KEY (bl_part_id, item_type)
        )
        """
    )
    con.commit()


def _read_csv(path: Path) -> Tuple[List[str], Dict[Tuple[str, str], Dict[str, str]]]:
    if not path.exists():
        return (["bl_part_id", "bk_part_id", "item_type", "brikick_name", "api_item_type", "bk_part_key"], {})
    with path.open("r", encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        header = r.fieldnames or []
        rows: Dict[Tuple[str, str], Dict[str, str]] = {}
        for row in r:
            bl = (row.get("bl_part_id") or "").strip()
            it = (row.get("item_type") or "").strip() or "P"
            if not bl:
                continue
            rows[(bl, it)] = {k: (v.strip() if isinstance(v, str) else v) for k, v in row.items()}
        # Ensure required columns exist in header order
        required = ["bl_part_id", "bk_part_id", "item_type", "brikick_name", "api_item_type", "bk_part_key"]
        for col in required:
            if col not in header:
                header.append(col)
        return header, rows


def _extract_n_from_key(key: str) -> Optional[int]:
    m = BK_KEY_RE.match(key.strip())
    if not m:
        return None
    return int(m.group(2))


def _compute_last_numbers(con: sqlite3.Connection, csv_rows: Dict[Tuple[str, str], Dict[str, str]]) -> Dict[str, int]:
    last: Dict[str, int] = {k: 0 for k in TYPE_META.keys()}
    # From CSV
    for (bl, it), row in csv_rows.items():
        key = (row.get("bk_part_key") or "").strip()
        n = _extract_n_from_key(key) if key else None
        if n is not None:
            last[it] = max(last.get(it, 0), n)

    # From DB existing values (covers cases where DB is ahead of CSV)
    cur = con.cursor()
    for it in TYPE_META.keys():
        for (key,) in cur.execute(
            "SELECT bk_part_key FROM brickovery_db WHERE item_type=? AND bk_part_key IS NOT NULL",
            (it,),
        ):
            if not key:
                continue
            n = _extract_n_from_key(str(key))
            if n is not None:
                last[it] = max(last.get(it, 0), n)
    return last


def _distinct_missing_pairs(con: sqlite3.Connection) -> List[Tuple[str, str]]:
    cur = con.cursor()
    out: List[Tuple[str, str]] = []
    for bl, it in cur.execute(
        """
        SELECT DISTINCT bl_part_id, item_type
        FROM brickovery_db
        WHERE (bk_part_id IS NULL OR bk_part_id='')
           OR (bk_part_key IS NULL OR bk_part_key='')
           OR (api_item_type IS NULL OR api_item_type='')
           OR (brikick_name IS NULL OR brikick_name='')
        ORDER BY item_type, bl_part_id
        """
    ):
        out.append((str(bl), (str(it) if it else "P")))
    return out


def _upsert_db(con: sqlite3.Connection, bl: str, it: str, bk_part_id: str, brikick_name: str, api_item_type: str, bk_part_key: str) -> None:
    cur = con.cursor()
    # Update all colors for (bl,item_type)
    cur.execute(
        """
        UPDATE brickovery_db
        SET bk_part_id=?, brikick_name=?, api_item_type=?, bk_part_key=?
        WHERE bl_part_id=? AND item_type=?
        """,
        (bk_part_id, brikick_name, api_item_type, bk_part_key, bl, it),
    )
    # Maintain internal mapping table
    cur.execute(
        """
        INSERT OR REPLACE INTO bk_mapping (bl_part_id, item_type, bk_part_id, brikick_name, api_item_type, bk_part_key)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (bl, it, bk_part_id, brikick_name, api_item_type, bk_part_key),
    )


def _append_new_rows(csv_path: Path, header: List[str], new_rows: List[Dict[str, str]]) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    exists = csv_path.exists()
    mode = "a" if exists else "w"
    with csv_path.open(mode, encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        if not exists:
            w.writeheader()
        for row in new_rows:
            # Ensure all header cols present
            out = {h: row.get(h, "") for h in header}
            w.writerow(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True, help="Path to brickovery.db")
    ap.add_argument("--bk-mapping-csv", required=True, help="Path to bk_mapping.csv (checked out from mapping repo)")
    ap.add_argument("--write-csv", action="store_true", help="Append auto-generated mappings into bk_mapping.csv")
    args = ap.parse_args()

    db_path = Path(args.db)
    csv_path = Path(args.bk_mapping_csv)

    con = sqlite3.connect(str(db_path))
    try:
        _ensure_columns(con)

        header, csv_rows = _read_csv(csv_path)
        last_numbers = _compute_last_numbers(con, csv_rows)

        missing_pairs = _distinct_missing_pairs(con)

        new_rows: List[Dict[str, str]] = []
        updated = 0
        created = 0

        for bl, it in missing_pairs:
            it = it.strip() or "P"
            if it not in TYPE_META:
                # Default unknowns to Parts (P) unless you later extend TYPE_META
                it = "P"

            # If mapping exists in CSV, use it
            row = csv_rows.get((bl, it))
            if row:
                bk_part_id = (row.get("bk_part_id") or "").strip()
                brikick_name = (row.get("brikick_name") or "").strip() or TYPE_META[it][0]
                api_item_type = (row.get("api_item_type") or "").strip() or TYPE_META[it][1]
                bk_part_key = (row.get("bk_part_key") or "").strip()

                # If key missing/invalid, regenerate deterministically
                n = _extract_n_from_key(bk_part_key) if bk_part_key else None
                if n is None:
                    last_numbers[it] = last_numbers.get(it, 0) + 1
                    n = last_numbers[it]
                    bk_part_id = bk_part_id or str(n)
                    bk_part_key = f"BK-{it}-{n:08d}"
                    # Update CSV cache (will be written only if --write-csv)
                    row["bk_part_id"] = bk_part_id
                    row["brikick_name"] = brikick_name
                    row["api_item_type"] = api_item_type
                    row["bk_part_key"] = bk_part_key
                    new_rows.append({**{k: "" for k in header}, **row})  # append a corrected line (optional)
                _upsert_db(con, bl, it, bk_part_id, brikick_name, api_item_type, bk_part_key)
                updated += 1
                continue

            # Otherwise: create new mapping row
            last_numbers[it] = last_numbers.get(it, 0) + 1
            n = last_numbers[it]
            brikick_name, api_item_type = TYPE_META[it]
            bk_part_id = str(n)
            bk_part_key = f"BK-{it}-{n:08d}"

            new_row = {
                "bl_part_id": bl,
                "bk_part_id": bk_part_id,
                "item_type": it,
                "brikick_name": brikick_name,
                "api_item_type": api_item_type,
                "bk_part_key": bk_part_key,
            }
            csv_rows[(bl, it)] = new_row
            new_rows.append(new_row)
            _upsert_db(con, bl, it, bk_part_id, brikick_name, api_item_type, bk_part_key)
            created += 1

        con.commit()

        if args.write_csv and new_rows:
            # Important: avoid duplicating "corrected existing rows" if file already has them.
            # For simplicity, we append; downstream can de-duplicate by (bl_part_id,item_type) if needed.
            _append_new_rows(csv_path, header, new_rows)

        print(f"[BK_MAPPING] missing_pairs={len(missing_pairs)} updated_from_csv={updated} created_new={created} csv_appended={len(new_rows) if args.write_csv else 0}")
        return 0
    finally:
        con.close()


if __name__ == "__main__":
    raise SystemExit(main())
