#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Export a dedicated BL -> BK mapping file from brickovery.db.

Output columns:
  bl_part_id,bk_part_id,item_type,bk_part_key,brikick_name,api_item_type

Note:
- bk_part_key is derived from DB columns: BK-{item_type}-{bk_part_id}-{bk_color_id}
- This export can contain multiple rows for the same (bl_part_id,item_type) across colors.

This file is required as a stable, standalone artifact for consumers.
"""

from __future__ import annotations

import argparse
import csv
import sqlite3
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="database/brickovery.db")
    ap.add_argument("--out", default="database/bl_to_bk_mapping.csv")
    args = ap.parse_args()

    db_path = Path(args.db)
    out_path = Path(args.out)

    if not db_path.exists():
        raise SystemExit(f"DB not found: {db_path}")

    out_path.parent.mkdir(parents=True, exist_ok=True)

    con = sqlite3.connect(str(db_path))
    cur = con.cursor()
    try:
        rows = cur.execute(
            """
            SELECT DISTINCT
              bl_part_id,
              bk_part_id,
              item_type,
              ('BK-' || item_type || '-' || bk_part_id || '-' || bk_color_id) AS bk_part_key,
              brikick_name,
              api_item_type
            FROM brickovery_db
            WHERE bk_part_id IS NOT NULL AND bk_part_id <> ''
              AND bk_color_id IS NOT NULL
            ORDER BY item_type, bl_part_id, bl_color_id
            """
        ).fetchall()
    finally:
        con.close()

    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["bl_part_id", "bk_part_id", "item_type", "bk_part_key", "brikick_name", "api_item_type"])
        for r in rows:
            w.writerow(r)

    print(f"[EXPORT] wrote {len(rows)} rows -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
