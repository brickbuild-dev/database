#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apply/ensure BK mapping into the final SQLite DB.

Goal:
- Ensure brickovery_db table contains (and is populated with):
  bl_part_id, bk_part_id, item_type, brikick_name, api_item_type, bk_part_key

Behavior:
- Loads bk_mapping.csv (must contain at least bl_part_id,bk_part_id,item_type,brikick_name,api_item_type; extra columns are tolerated).
- For any (bl_part_id,item_type) present in DB and missing in CSV:
    * auto-generates a new bk_part_id using per-item_type counters (no collisions),
    * appends the new row to bk_mapping.csv (optional),
    * updates brickovery_db columns for all colors for that (bl_part_id,item_type).
- bk_part_key is derived from DB columns: BK-{item_type}-{bk_part_id}-{bk_color_id}.
- Also maintains an internal table bk_mapping (optional but useful) inside the same DB.

This script is designed to run *after* brickovery_upstream_v3.py builds/updates the DB.
"""

from __future__ import annotations

import argparse
import csv
import io
import datetime
import hashlib
import os
import sqlite3
from pathlib import Path
from typing import Dict, List, Tuple, Optional

BK_PART_KEY_FORMAT = "BK-{item_type}-{bk_part_id}-{bk_color_id}"
CSV_REQUIRED_COLUMNS = ["bl_part_id", "bk_part_id", "item_type", "brikick_name", "api_item_type"]
CSV_DROP_COLUMNS = {"bk_part_key", "source", "confidence"}

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

def _utc_stamp() -> Tuple[str, str]:
    """Return (stamp_for_filename, human_readable) in UTC."""
    now = datetime.datetime.utcnow().replace(microsecond=0)
    stamp = now.strftime("%Y%m%d_%H%M%SZ")
    human = now.strftime("%Y-%m-%d %H:%M:%SZ")
    return stamp, human


def _sha256_bytes(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _unique_path(path: Path) -> Path:
    """Ensure path is unique by adding a numeric suffix if needed."""
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    i = 1
    while True:
        candidate = parent / f"{stem}__{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def _write_backup_pre_update(csv_path: Path, stamp: str, human: str) -> Optional[Path]:
    """Create an immutable backup snapshot of the current CSV before modifying it."""
    if not csv_path.exists():
        return None

    backups_dir = csv_path.parent / "backups"
    backups_dir.mkdir(parents=True, exist_ok=True)

    backup_path = _unique_path(backups_dir / f"bk_mapping_backup_{stamp}.csv")
    raw = csv_path.read_bytes()
    sha = _sha256_bytes(raw)

    header_lines = [
        f"# Brikick BK Mapping Backup",
        f"# created_at_utc={human}",
        f"# source_file={csv_path.name}",
        f"# source_sha256={sha}",
        f"# NOTE: This backup is immutable. Do not edit. Use for emergency rollback.",
        "",
    ]
    with backup_path.open("wb") as f:
        f.write(("\n".join(header_lines)).encode("utf-8"))
        f.write(raw)
    return backup_path


def _write_change_report(
    base_dir: Path,
    stamp: str,
    human: str,
    csv_name: str,
    previous_sha: Optional[str],
    new_sha: Optional[str],
    previous_rows: int,
    new_rows_count: int,
    changes: List[Dict[str, str]],
    backup_path: Optional[Path],
) -> Path:
    """Write a detailed immutable report about the modifications performed."""
    audit_dir = base_dir / "audit"
    audit_dir.mkdir(parents=True, exist_ok=True)
    report_path = _unique_path(audit_dir / f"bk_mapping_changes_{stamp}.md")

    lines: List[str] = []
    lines.append(f"# BK Mapping Change Report — {stamp}")
    lines.append("")
    lines.append(f"created_at_utc: {human}")
    lines.append(f"target_csv: {csv_name}")
    if backup_path:
        lines.append(f"backup_file: {backup_path.as_posix()}")
    lines.append(f"previous_sha256: {previous_sha or ''}")
    lines.append(f"new_sha256: {new_sha or ''}")
    lines.append(f"previous_row_count: {previous_rows}")
    lines.append(f"new_row_count: {new_rows_count}")
    lines.append(f"change_count: {len(changes)}")
    lines.append("")
    lines.append("## Changes")
    lines.append("")
    if not changes:
        lines.append("- (no changes)")
    else:
        for ch in changes:
            # action: created/corrected/filled
            action = ch.get("action", "")
            bl = ch.get("bl_part_id", "")
            it = ch.get("item_type", "")
            bk_id = ch.get("bk_part_id", "")
            brikick_name = ch.get("brikick_name", "")
            api_item_type = ch.get("api_item_type", "")
            note = ch.get("note", "")
            lines.append(f"- **{action}** bl_part_id=`{bl}` item_type=`{it}` bk_part_id=`{bk_id}` brikick_name=`{brikick_name}` api_item_type=`{api_item_type}`{(' — ' + note) if note else ''}")

    lines.append("")
    lines.append("## Operational notes")
    lines.append("")
    lines.append("- This report is immutable (never overwrite previous reports).")
    lines.append("- Timestamp is embedded in both the filename and the body for emergency traceability.")
    lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def _write_csv_canonical(csv_path: Path, header: List[str], rows: Dict[Tuple[str, str], Dict[str, str]]) -> None:
    """Rewrite bk_mapping.csv canonically (unique by (bl_part_id,item_type))."""
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    # Stable sort: by item_type then numeric bk_part_id (if any), then bl_part_id
    def sort_key(item):
        (bl, it), row = item
        bk_id = (row.get("bk_part_id") or "").strip()
        n = int(bk_id) if bk_id.isdigit() else 0
        return (it, n, bl)

    tmp = csv_path.parent / f".tmp_bk_mapping_{os.getpid()}.csv"
    with tmp.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        w.writeheader()
        for (_, _), row in sorted(rows.items(), key=sort_key):
            out = {h: row.get(h, "") for h in header}
            w.writerow(out)
    tmp.replace(csv_path)


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
    required = CSV_REQUIRED_COLUMNS.copy()
    if not path.exists():
        return (required.copy(), {})

    raw = path.read_text(encoding="utf-8", errors="replace").splitlines()
    # Allow comment/metadata lines in backups or in emergency-reverted files
    filtered = [ln for ln in raw if ln.strip() and not ln.lstrip().startswith("#")]
    if not filtered:
        return (required.copy(), {})

    with io.StringIO("\n".join(filtered) + "\n") as f:
        r = csv.DictReader(f)
        header = (r.fieldnames or []).copy()
        rows: Dict[Tuple[str, str], Dict[str, str]] = {}
        for row in r:
            bl = (row.get("bl_part_id") or "").strip()
            it = (row.get("item_type") or "").strip() or "U"
            if not bl:
                continue
            rows[(bl, it)] = {k: (v.strip() if isinstance(v, str) else v) for k, v in row.items()}

        for col in required:
            if col not in header:
                header.append(col)
        return header, rows


def _normalize_header(header: List[str]) -> List[str]:
    out: List[str] = []
    for col in header:
        if col in CSV_DROP_COLUMNS:
            continue
        if col not in out:
            out.append(col)
    for col in CSV_REQUIRED_COLUMNS:
        if col not in out:
            out.append(col)
    return out


def _compute_last_numbers(con: sqlite3.Connection, csv_rows: Dict[Tuple[str, str], Dict[str, str]]) -> Dict[str, int]:
    last: Dict[str, int] = {k: 0 for k in TYPE_META.keys()}
    # From CSV
    for (bl, it), row in csv_rows.items():
        bk_id = (row.get("bk_part_id") or "").strip()
        if bk_id.isdigit():
            last[it] = max(last.get(it, 0), int(bk_id))

    # From DB existing values (covers cases where DB is ahead of CSV)
    cur = con.cursor()
    for it in TYPE_META.keys():
        for (bk_id,) in cur.execute(
            "SELECT bk_part_id FROM brickovery_db WHERE item_type=? AND bk_part_id IS NOT NULL",
            (it,),
        ):
            if not bk_id:
                continue
            s = str(bk_id).strip()
            if s.isdigit():
                last[it] = max(last.get(it, 0), int(s))
    return last


def _db_existing_bk_part_id(con: sqlite3.Connection, bl: str, it: str) -> Optional[str]:
    cur = con.cursor()
    row = cur.execute(
        """
        SELECT bk_part_id
        FROM brickovery_db
        WHERE bl_part_id=? AND item_type=? AND bk_part_id IS NOT NULL AND bk_part_id<>''
        LIMIT 1
        """,
        (bl, it),
    ).fetchone()
    if not row or row[0] is None:
        return None
    s = str(row[0]).strip()
    return s if s.isdigit() else None


def _distinct_missing_pairs(con: sqlite3.Connection) -> List[Tuple[str, str]]:
    cur = con.cursor()
    out: List[Tuple[str, str]] = []
    for bl, it in cur.execute(
        """
        SELECT DISTINCT bl_part_id, item_type
        FROM brickovery_db
        WHERE (bk_part_id IS NULL OR bk_part_id='')
           OR (api_item_type IS NULL OR api_item_type='')
           OR (brikick_name IS NULL OR brikick_name='')
        ORDER BY item_type, bl_part_id
        """
    ):
        out.append((str(bl), (str(it) if it else "P")))
    return out


def _upsert_db(con: sqlite3.Connection, bl: str, it: str, bk_part_id: str, brikick_name: str, api_item_type: str) -> None:
    cur = con.cursor()
    # Update all colors for (bl,item_type)
    cur.execute(
        """
        UPDATE brickovery_db
        SET bk_part_id=?, brikick_name=?, api_item_type=?,
            bk_part_key=('BK-' || item_type || '-' || bk_part_id || '-' || bk_color_id)
        WHERE bl_part_id=? AND item_type=?
        """,
        (bk_part_id, brikick_name, api_item_type, bl, it),
    )
    # Maintain internal mapping table
    cur.execute(
        """
        INSERT OR REPLACE INTO bk_mapping (bl_part_id, item_type, bk_part_id, brikick_name, api_item_type, bk_part_key)
        VALUES (?, ?, ?, ?, ?, NULL)
        """,
        (bl, it, bk_part_id, brikick_name, api_item_type),
    )


def _append_new_rows(csv_path: Path, header: List[str], new_rows: List[Dict[str, str]]) -> None:
    """Backward-compatible wrapper.

    NOTE: For safety and to avoid duplicates in a vital mapping file, we rewrite canonically
    instead of appending blindly.
    """
    # Read existing, merge, then canonical rewrite.
    hdr, rows = _read_csv(csv_path)
    # Ensure header contains any new columns
    for col in header:
        if col not in hdr:
            hdr.append(col)
    for row in new_rows:
        bl = (row.get("bl_part_id") or "").strip()
        it = (row.get("item_type") or "").strip() or "U"
        if not bl:
            continue
        rows[(bl, it)] = {**rows.get((bl, it), {}), **row}
    _write_csv_canonical(csv_path, hdr, rows)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True, help="Path to brickovery.db")
    ap.add_argument("--bk-mapping-csv", required=True, help="Path to bk_mapping.csv (checked out from mapping repo)")
    ap.add_argument("--write-csv", action="store_true", help="Write/refresh auto-generated mappings into bk_mapping.csv")
    args = ap.parse_args()

    db_path = Path(args.db)
    csv_path = Path(args.bk_mapping_csv)

    con = sqlite3.connect(str(db_path))
    try:
        _ensure_columns(con)

        header, csv_rows = _read_csv(csv_path)
        target_header = _normalize_header(header)
        last_numbers = _compute_last_numbers(con, csv_rows)

        missing_pairs = _distinct_missing_pairs(con)

        new_rows: List[Dict[str, str]] = []
        updated = 0
        created = 0
        changes: List[Dict[str, str]] = []
        header_changed = header != target_header

        for bl, it in missing_pairs:
            it = (it or '').strip() or 'U'
            if len(it) != 1:
                it = 'U'
            if it not in TYPE_META:
                # Default unknowns to Unsorted Lots (U) as the last-resort category
                it = "U"

            # If mapping exists in CSV, use it (and fill/correct missing fields if needed)
            row = csv_rows.get((bl, it))
            if row:
                # Keep originals for audit
                orig_bk_part_id = (row.get("bk_part_id") or "").strip()
                orig_brikick_name = (row.get("brikick_name") or "").strip()
                orig_api_item_type = (row.get("api_item_type") or "").strip()

                bk_part_id = orig_bk_part_id
                brikick_name = orig_brikick_name or TYPE_META[it][0]
                api_item_type = orig_api_item_type or TYPE_META[it][1]

                # Determine numeric id n:
                # 1) from numeric bk_part_id (if present)
                # 2) allocate next per-item_type
                n: Optional[int] = None
                if bk_part_id and bk_part_id.isdigit():
                    n = int(bk_part_id)
                if n is None:
                    last_numbers[it] = last_numbers.get(it, 0) + 1
                    n = last_numbers[it]
                else:
                    # Ensure counters won't collide with existing n
                    last_numbers[it] = max(last_numbers.get(it, 0), n)

                changed_fields: List[str] = []

                # Fill missing or non-numeric bk_part_id
                if (not bk_part_id) or (not bk_part_id.isdigit()):
                    bk_part_id = str(n)
                    row["bk_part_id"] = bk_part_id
                    changed_fields.append("bk_part_id")

                # Fill brikick_name/api_item_type if blank
                if not orig_brikick_name:
                    row["brikick_name"] = brikick_name
                    changed_fields.append("brikick_name")
                if not orig_api_item_type:
                    row["api_item_type"] = api_item_type
                    changed_fields.append("api_item_type")

                # Record changes for audit + CSV write
                if changed_fields:
                    changes.append({
                        "action": "corrected_existing",
                        "bl_part_id": bl,
                        "item_type": it,
                        "bk_part_id": bk_part_id,
                        "brikick_name": brikick_name,
                        "api_item_type": api_item_type,
                        "note": "filled/normalized: " + ", ".join(changed_fields),
                    })
                    new_rows.append({**row})  # mark that CSV should be updated

                _upsert_db(con, bl, it, bk_part_id, brikick_name, api_item_type)
                updated += 1
                continue

            # Otherwise: create new mapping row
            existing_id = _db_existing_bk_part_id(con, bl, it)
            if existing_id:
                bk_part_id = existing_id
                n = int(existing_id)
                last_numbers[it] = max(last_numbers.get(it, 0), n)
            else:
                last_numbers[it] = last_numbers.get(it, 0) + 1
                n = last_numbers[it]
                bk_part_id = str(n)

            brikick_name, api_item_type = TYPE_META[it]

            new_row = {
                "bl_part_id": bl,
                "bk_part_id": bk_part_id,
                "item_type": it,
                "brikick_name": brikick_name,
                "api_item_type": api_item_type,
            }
            csv_rows[(bl, it)] = new_row
            new_rows.append(new_row)
            changes.append({
                "action": "created_new",
                "bl_part_id": bl,
                "item_type": it,
                "bk_part_id": bk_part_id,
                "brikick_name": brikick_name,
                "api_item_type": api_item_type,
                "note": "auto-generated (not present in bk_mapping.csv)",
            })
            _upsert_db(con, bl, it, bk_part_id, brikick_name, api_item_type)
            created += 1

        # Ensure bk_part_key uses the new canonical format for all rows
        try:
            con.execute(
                "UPDATE brickovery_db SET bk_part_key=('BK-' || item_type || '-' || bk_part_id || '-' || bk_color_id)"
            )
        except Exception:
            pass

        con.commit()

        if args.write_csv and (new_rows or header_changed):
            # Vital data protection:
            # - Create an immutable pre-update backup snapshot
            # - Rewrite canonically (no duplicates) to keep mapping deterministic
            # - Emit an immutable, timestamped change report
            stamp, human = _utc_stamp()

            # Capture previous state (if any)
            prev_sha = _sha256_file(csv_path) if csv_path.exists() else None
            prev_header, prev_rows = _read_csv(csv_path)
            prev_count = len(prev_rows)

            backup_path = _write_backup_pre_update(csv_path, stamp, human)

            # Canonical rewrite with updated rows
            _write_csv_canonical(csv_path, target_header, csv_rows)

            new_sha = _sha256_file(csv_path) if csv_path.exists() else None
            new_count = len(csv_rows)

            report_path = _write_change_report(
                csv_path.parent,
                stamp,
                human,
                csv_path.name,
                prev_sha,
                new_sha,
                prev_count,
                new_count,
                changes,
                backup_path,
            )

            print(f"[BK_MAPPING_AUDIT] backup={backup_path.as_posix() if backup_path else ''} report={report_path.as_posix()}")

        print(f"[BK_MAPPING] missing_pairs={len(missing_pairs)} updated_from_csv={updated} created_new={created} csv_appended={len(new_rows) if args.write_csv else 0}")
        return 0
    finally:
        con.close()


if __name__ == "__main__":
    raise SystemExit(main())
