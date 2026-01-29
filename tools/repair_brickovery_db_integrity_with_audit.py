#!/usr/bin/env python3
"""
repair_brickovery_db_integrity_with_audit.py

Repairs a specific corruption pattern in SQLite table `brickovery_db` where:
  - bl_part_id accidentally contains a 1-letter item_type (P/S/M/B/G/C/I/O/U)
  - item_type accidentally contains the actual BrickLink item id (length>1)

This script swaps (bl_part_id, item_type) for the affected rows, safely:
  - INSERT OR IGNORE corrected rows
  - DELETE corrupted rows
This avoids conflicts when unique constraints exist.

Additionally, it writes an immutable audit report file (timestamped) describing
exactly what changed.

Usage:
  python tools/repair_brickovery_db_integrity_with_audit.py --db database/brickovery.db
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import os
from pathlib import Path
import sqlite3
from typing import List, Tuple, Dict, Any

TYPE_LETTERS = ("P", "S", "M", "B", "G", "C", "I", "O", "U")

def _utc_stamp() -> str:
    return _dt.datetime.utcnow().strftime("%Y%m%d_%H%M%SZ")

def _sha256_file(path: Path, chunk: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def _ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def _qident(name: str) -> str:
    # SQLite identifier quoting (double quotes); escape any embedded quotes.
    return '"' + name.replace('"', '""') + '"'

def _table_columns(con: sqlite3.Connection, table: str) -> List[str]:
    cur = con.execute(f"PRAGMA table_info({_qident(table)})")
    cols = [r[1] for r in cur.fetchall()]  # (cid, name, type, notnull, dflt_value, pk)
    if not cols:
        raise SystemExit(f"ERROR: table '{table}' not found or has no columns.")
    return cols

def _count(con: sqlite3.Connection, sql: str, params: Tuple[Any, ...] = ()) -> int:
    cur = con.execute(sql, params)
    row = cur.fetchone()
    return int(row[0]) if row and row[0] is not None else 0

def _candidate_rows(con: sqlite3.Connection, table: str, limit_samples: int) -> List[Tuple[int, str, str, Any]]:
    # Return (rowid, bl_part_id, item_type, bl_color_id) for audit samples.
    sql = f"""
      SELECT rowid, bl_part_id, item_type,
             CASE WHEN EXISTS(SELECT 1 FROM pragma_table_info({_qident(table)}) WHERE name='bl_color_id')
                  THEN bl_color_id
                  ELSE NULL
             END AS bl_color_id
      FROM {_qident(table)}
      WHERE bl_part_id IN ({",".join("?" for _ in TYPE_LETTERS)})
        AND item_type IS NOT NULL
        AND length(item_type) > 1
        AND item_type NOT IN ({",".join("?" for _ in TYPE_LETTERS)})
      LIMIT ?
    """
    params = TYPE_LETTERS + TYPE_LETTERS + (limit_samples,)
    cur = con.execute(sql, params)
    return [(int(r[0]), str(r[1]), str(r[2]), r[3]) for r in cur.fetchall()]

def main() -> int:
    ap = argparse.ArgumentParser(description="Repair corrupted (bl_part_id,item_type) swaps and write an audit report.")
    ap.add_argument("--db", required=True, help="Path to SQLite database (e.g., database/brickovery.db)")
    ap.add_argument("--table", default="brickovery_db", help="Table to repair (default: brickovery_db)")
    ap.add_argument("--audit-dir", default="database/audit/brickovery_db", help="Directory to write audit files")
    ap.add_argument("--max-samples", type=int, default=200, help="Max sample rows to include in audit (default: 200)")
    ap.add_argument("--dry-run", action="store_true", help="Do not modify DB; only produce audit report")
    args = ap.parse_args()

    db_path = Path(args.db)
    if not db_path.exists():
        raise SystemExit(f"ERROR: DB not found: {db_path}")

    audit_dir = Path(args.audit_dir)
    _ensure_dir(audit_dir)

    stamp = _utc_stamp()
    audit_path = audit_dir / f"brickovery_db_repair_{stamp}.md"

    db_sha_before = _sha256_file(db_path)
    db_size_before = db_path.stat().st_size

    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row

    try:
        cols = _table_columns(con, args.table)

        total_before = _count(con, f"SELECT COUNT(*) FROM {_qident(args.table)}")
        # count candidates (same predicate as samples but without LIMIT)
        cand_sql = f"""
          SELECT COUNT(*)
          FROM {_qident(args.table)}
          WHERE bl_part_id IN ({",".join("?" for _ in TYPE_LETTERS)})
            AND item_type IS NOT NULL
            AND length(item_type) > 1
            AND item_type NOT IN ({",".join("?" for _ in TYPE_LETTERS)})
        """
        cand_params = TYPE_LETTERS + TYPE_LETTERS
        candidates = _count(con, cand_sql, cand_params)

        samples = _candidate_rows(con, args.table, max(0, args.max_samples))

        inserted = 0
        deleted = 0
        remaining_bad = candidates

        if not args.dry_run and candidates > 0:
            con.execute("BEGIN IMMEDIATE")

            # Build INSERT OR IGNORE ... SELECT ... swapping bl_part_id and item_type.
            col_list = ", ".join(_qident(c) for c in cols)
            select_exprs = []
            for c in cols:
                if c == "bl_part_id":
                    select_exprs.append("item_type AS bl_part_id")
                elif c == "item_type":
                    select_exprs.append("bl_part_id AS item_type")
                else:
                    select_exprs.append(_qident(c))
            select_list = ", ".join(select_exprs)

            where_pred = f"""
              bl_part_id IN ({",".join("?" for _ in TYPE_LETTERS)})
              AND item_type IS NOT NULL
              AND length(item_type) > 1
              AND item_type NOT IN ({",".join("?" for _ in TYPE_LETTERS)})
            """
            ins_sql = f"INSERT OR IGNORE INTO {_qident(args.table)} ({col_list}) SELECT {select_list} FROM {_qident(args.table)} WHERE {where_pred}"
            con.execute(ins_sql, cand_params)
            inserted = _count(con, "SELECT changes()")

            del_sql = f"DELETE FROM {_qident(args.table)} WHERE {where_pred}"
            con.execute(del_sql, cand_params)
            deleted = _count(con, "SELECT changes()")

            con.commit()

            remaining_bad = _count(con, cand_sql, cand_params)

        total_after = _count(con, f"SELECT COUNT(*) FROM {_qident(args.table)}")

    finally:
        con.close()

    db_sha_after = _sha256_file(db_path)
    db_size_after = db_path.stat().st_size

    # Write audit report (immutable, timestamped)
    lines = []
    lines.append(f"# Brickovery DB Repair Audit\n")
    lines.append(f"- created_at_utc: `{stamp}`\n")
    lines.append(f"- db_path: `{db_path.as_posix()}`\n")
    lines.append(f"- table: `{args.table}`\n")
    lines.append(f"- dry_run: `{bool(args.dry_run)}`\n")
    lines.append("\n## DB fingerprint\n")
    lines.append(f"- sha256_before: `{db_sha_before}`\n")
    lines.append(f"- size_before_bytes: `{db_size_before}`\n")
    lines.append(f"- sha256_after: `{db_sha_after}`\n")
    lines.append(f"- size_after_bytes: `{db_size_after}`\n")

    lines.append("\n## Detection summary\n")
    lines.append(f"- total_rows_before: `{total_before}`\n")
    lines.append(f"- candidate_corrupted_rows: `{candidates}`\n")

    if args.dry_run:
        lines.append("\n## Action\n")
        lines.append("- No DB changes were applied (dry run).\n")
    else:
        lines.append("\n## Action applied\n")
        lines.append("Repair strategy: `INSERT OR IGNORE corrected rows (swap bl_part_id<->item_type)`, then `DELETE corrupted rows`.\n")
        lines.append(f"- inserted_corrected_rows: `{inserted}`\n")
        lines.append(f"- deleted_corrupted_rows: `{deleted}`\n")
        lines.append(f"- remaining_corrupted_rows_after: `{remaining_bad}`\n")
        lines.append(f"- total_rows_after: `{total_after}`\n")

    lines.append("\n## Sample of affected rows (before → after)\n")
    if samples:
        lines.append("| rowid | bl_part_id(before) | item_type(before) | bl_color_id | bl_part_id(after) | item_type(after) |\n")
        lines.append("|---:|---|---|---:|---|---|\n")
        for rowid, blpid, itype, colorid in samples:
            # after swap:
            lines.append(f"| {rowid} | `{blpid}` | `{itype}` | `{'' if colorid is None else colorid}` | `{itype}` | `{blpid}` |\n")
        if candidates > len(samples):
            lines.append(f"\n> Note: only first {len(samples)} rows shown (limit). Total candidates: {candidates}.\n")
    else:
        lines.append("_No candidate rows found (or max-samples=0)._ \n")

    audit_path.write_text("".join(lines), encoding="utf-8")

    # Emit a small JSON line for workflow consumption if desired.
    print(f'{{"repair_candidates": {candidates}, "repaired_inserted": {inserted}, "repaired_deleted": {deleted}, "remaining_bad": {remaining_bad}, "audit_file": "{audit_path.as_posix()}"}}')
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
