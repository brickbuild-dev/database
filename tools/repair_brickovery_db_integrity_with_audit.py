#!/usr/bin/env python3
"""Repair brickovery.db integrity after upstream semantic delta.

Fixes the failure mode where part_color_codes tuples were swapped, producing rows like:
  bl_part_id='P', item_type='3001', bl_color_id=...
The repair is *in-place* (no rebuild) and is safe to run repeatedly.

Actions:
  1) Swap (bl_part_id, item_type) for rows where bl_part_id is a 1-letter type token and item_type is not.
  2) Normalize item_type to the allowed canonical set: P,S,M,B,G,C,I,O,U
     - common long forms (PART/SET/MINIFIG/...) are mapped
     - unknowns collapse to U

Exits 0; prints a small JSON summary to stdout.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path
from typing import List

ALLOWED = ("P","S","M","B","G","C","I","O","U")


def _cols(cur: sqlite3.Cursor, table: str) -> List[str]:
    return [r[1] for r in cur.execute(f"PRAGMA table_info({table})").fetchall()]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True)
    ap.add_argument("--table", default="brickovery_db")
    args = ap.parse_args()

    db = Path(args.db)
    table = args.table

    con = sqlite3.connect(str(db))
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    try:
        cols = _cols(cur, table)
        if not cols:
            raise SystemExit(f"Table not found: {table}")

        # --- Step 1: swap corrupted rows in one shot ---
        # Condition: bl_part_id is a type token AND item_type is not a canonical type token.
        cond = (
            f"(bl_part_id IN ({','.join(['?']*len(ALLOWED))})) "
            f"AND (item_type IS NOT NULL AND TRIM(item_type) <> '') "
            f"AND (UPPER(TRIM(item_type)) NOT IN ({','.join(['?']*len(ALLOWED))}) OR LENGTH(TRIM(item_type)) <> 1)"
        )
        params = list(ALLOWED) + list(ALLOWED)

        # Build INSERT columns and SELECT expressions with swapped keys
        insert_cols = ", ".join(cols)
        select_exprs = []
        for c in cols:
            if c == "bl_part_id":
                select_exprs.append("item_type AS bl_part_id")
            elif c == "item_type":
                select_exprs.append("bl_part_id AS item_type")
            else:
                select_exprs.append(c)
        select_cols = ", ".join(select_exprs)

        before_bad = cur.execute(f"SELECT COUNT(*) FROM {table} WHERE {cond}", params).fetchone()[0]

        if before_bad:
            cur.execute("BEGIN")
            cur.execute(
                f"""
                INSERT OR IGNORE INTO {table} ({insert_cols})
                SELECT {select_cols}
                FROM {table}
                WHERE {cond}
                """,
                params,
            )
            inserted = cur.rowcount  # sqlite rowcount is unreliable for INSERT..SELECT; we'll compute later

            cur.execute(f"DELETE FROM {table} WHERE {cond}", params)
            deleted = cur.rowcount
            con.commit()
        else:
            inserted = 0
            deleted = 0

        # --- Step 2: normalize item_type ---
        cur.execute("BEGIN")

        # Uppercase/trim
        cur.execute(f"UPDATE {table} SET item_type = UPPER(TRIM(item_type)) WHERE item_type IS NOT NULL")

        # Map long forms
        cur.execute(f"UPDATE {table} SET item_type='P' WHERE item_type IN ('PART','PARTS')")
        cur.execute(f"UPDATE {table} SET item_type='S' WHERE item_type IN ('SET','SETS')")
        cur.execute(f"UPDATE {table} SET item_type='M' WHERE item_type IN ('MINIFIG','MINIFIGS')")
        cur.execute(f"UPDATE {table} SET item_type='B' WHERE item_type IN ('BOOK','BOOKS')")
        cur.execute(f"UPDATE {table} SET item_type='G' WHERE item_type IN ('GEAR','GEARS')")
        cur.execute(f"UPDATE {table} SET item_type='C' WHERE item_type IN ('CATALOG','CATALOGS')")
        cur.execute(f"UPDATE {table} SET item_type='I' WHERE item_type IN ('INSTRUCTION','INSTRUCTIONS')")
        cur.execute(f"UPDATE {table} SET item_type='O' WHERE item_type IN ('ORIGINAL_BOX','ORIGINALBOX','ORIGINAL_BOXES','ORIGINALBOXES')")
        cur.execute(f"UPDATE {table} SET item_type='U' WHERE item_type IN ('UNSORTED_LOT','UNSORTED','UNKNOWN','OTHER')")

        # Collapse any remaining invalids to U
        cur.execute(
            f"UPDATE {table} SET item_type='U' "
            f"WHERE item_type IS NULL OR TRIM(item_type)='' "
            f"OR item_type NOT IN ({','.join(['?']*len(ALLOWED))})",
            list(ALLOWED),
        )
        normalized = cur.rowcount

        con.commit()

        # Count current invalids (should be 0)
        invalid_now = cur.execute(
            f"SELECT COUNT(*) FROM {table} WHERE item_type NOT IN ({','.join(['?']*len(ALLOWED))})",
            list(ALLOWED),
        ).fetchone()[0]

        out = {
            "bad_rows_before": before_bad,
            "swap_deleted": deleted,
            "normalized_item_type": normalized,
            "invalid_item_type_after": invalid_now,
        }
        print(json.dumps(out, ensure_ascii=False))
        return 0
    finally:
        con.close()


if __name__ == "__main__":
    raise SystemExit(main())
