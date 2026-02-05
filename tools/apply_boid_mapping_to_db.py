#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apply BL->BOID mapping from a CSV into brickovery.db.

Expected columns (flexible aliases):
  - bl_part_id (required)
  - boid (required)
  - bl_color_id (optional; if missing, applies to all colors)
  - item_type (optional; default=P)
"""

from __future__ import annotations

import argparse
import csv
import sqlite3
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


def _open_csv(path: Path) -> Tuple[Iterable[Dict[str, str]], List[str]]:
    sample = ""
    try:
        with path.open("r", encoding="utf-8-sig", errors="replace") as f:
            sample = f.read(4096)
    except FileNotFoundError:
        raise

    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
    except Exception:
        dialect = csv.excel
    dialect.skipinitialspace = True

    fh = path.open("r", newline="", encoding="utf-8-sig", errors="replace")
    reader = csv.DictReader(fh, dialect=dialect)
    fieldnames = [((fn or "").strip()) for fn in (reader.fieldnames or [])]
    reader.fieldnames = fieldnames
    return reader, fieldnames


def _pick(row: Dict[str, str], keys: List[str]) -> Optional[str]:
    for k in keys:
        v = row.get(k)
        if v is None:
            continue
        s = str(v).strip()
        if s != "":
            return s
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True, help="Path to brickovery.db")
    ap.add_argument("--csv", required=True, help="Path to bl_boid_mapping.csv")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing boid values (default: only fill NULL).")
    args = ap.parse_args()

    db_path = Path(args.db)
    csv_path = Path(args.csv)
    if not db_path.exists():
        raise SystemExit(f"DB not found: {db_path}")
    if not csv_path.exists():
        raise SystemExit(f"CSV not found: {csv_path}")

    reader, fieldnames = _open_csv(csv_path)
    if not fieldnames:
        raise SystemExit("CSV has no header.")

    part_keys = ["bl_part_id", "part_id", "item_id", "item_no", "itemid", "bl_item_no", "part"]
    color_keys = ["bl_color_id", "color_id", "bl_color", "color"]
    type_keys = ["item_type", "itemtype", "type"]
    boid_keys = ["boid", "bo_id", "brickowl_id"]

    with_color: List[Tuple[str, str, int, str]] = []
    no_color: List[Tuple[str, str, str]] = []
    skipped = 0

    for row in reader:
        bl = _pick(row, part_keys)
        boid = _pick(row, boid_keys)
        if not bl or not boid:
            skipped += 1
            continue
        it = (_pick(row, type_keys) or "P").strip().upper()
        color_val = _pick(row, color_keys)
        if color_val is None:
            no_color.append((boid, bl, it))
            continue
        try:
            blc = int(str(color_val).strip())
        except Exception:
            skipped += 1
            continue
        with_color.append((boid, bl, blc, it))

    con = sqlite3.connect(str(db_path))
    cur = con.cursor()
    updated = 0

    def _exec_many(sql: str, rows: List[Tuple], batch_size: int = 5000) -> int:
        total = 0
        for i in range(0, len(rows), batch_size):
            chunk = rows[i:i + batch_size]
            cur.executemany(sql, chunk)
            if cur.rowcount is not None and cur.rowcount > 0:
                total += int(cur.rowcount)
            con.commit()
        return total

    if with_color:
        if args.overwrite:
            sql = (
                "UPDATE brickovery_db SET boid=? "
                "WHERE bl_part_id=? AND bl_color_id=? AND item_type=?"
            )
        else:
            sql = (
                "UPDATE brickovery_db SET boid=? "
                "WHERE bl_part_id=? AND bl_color_id=? AND item_type=? "
                "AND (boid IS NULL OR boid='')"
            )
        updated += _exec_many(sql, with_color)

    if no_color:
        if args.overwrite:
            sql = (
                "UPDATE brickovery_db SET boid=? "
                "WHERE bl_part_id=? AND item_type=?"
            )
        else:
            sql = (
                "UPDATE brickovery_db SET boid=? "
                "WHERE bl_part_id=? AND item_type=? "
                "AND (boid IS NULL OR boid='')"
            )
        updated += _exec_many(sql, no_color)

    con.close()
    print(
        f"[BOID_MAPPING] rows_with_color={len(with_color)} rows_no_color={len(no_color)} "
        f"skipped={skipped} updated={updated}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
