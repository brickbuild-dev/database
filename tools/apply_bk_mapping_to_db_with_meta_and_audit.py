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
import io
import datetime
import hashlib
import os
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
            bk_key = ch.get("bk_part_key", "")
            brikick_name = ch.get("brikick_name", "")
            api_item_type = ch.get("api_item_type", "")
            note = ch.get("note", "")
            lines.append(f"- **{action}** bl_part_id=`{bl}` item_type=`{it}` bk_part_id=`{bk_id}` bk_part_key=`{bk_key}` brikick_name=`{brikick_name}` api_item_type=`{api_item_type}`{(' — ' + note) if note else ''}")

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

    # Stable sort: by item_type then numeric suffix of bk_part_key (if any), then bl_part_id
    def sort_key(item):
        (bl, it), row = item
        key = (row.get("bk_part_key") or "").strip()
        m = BK_KEY_RE.match(key)
        n = int(m.group(2)) if m else 0
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
    required = ["bl_part_id", "bk_part_id", "item_type", "brikick_name", "api_item_type", "bk_part_key"]
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
            it = (row.get("item_type") or "").strip() or "P"
            if not bl:
                continue
            rows[(bl, it)] = {k: (v.strip() if isinstance(v, str) else v) for k, v in row.items()}

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
        it = (row.get("item_type") or "").strip() or "P"
        if not bl:
            continue
        rows[(bl, it)] = {**rows.get((bl, it), {}), **row}
    _write_csv_canonical(csv_path, hdr, rows)

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
        changes: List[Dict[str, str]] = []

        for bl, it in missing_pairs:
            it = it.strip() or "P"
            if it not in TYPE_META:
                # Default unknowns to Parts (P) unless you later extend TYPE_META
                it = "P"

            # If mapping exists in CSV, use it (and fill/correct missing fields if needed)
            row = csv_rows.get((bl, it))
            if row:
                # Keep originals for audit
                orig_bk_part_id = (row.get("bk_part_id") or "").strip()
                orig_brikick_name = (row.get("brikick_name") or "").strip()
                orig_api_item_type = (row.get("api_item_type") or "").strip()
                orig_bk_part_key = (row.get("bk_part_key") or "").strip()

                bk_part_id = orig_bk_part_id
                brikick_name = orig_brikick_name or TYPE_META[it][0]
                api_item_type = orig_api_item_type or TYPE_META[it][1]
                bk_part_key = orig_bk_part_key

                # Determine numeric id n in the safest order:
                # 1) from bk_part_key (canonical)
                # 2) from numeric bk_part_id (if present)
                # 3) allocate next per-item_type
                n = _extract_n_from_key(bk_part_key) if bk_part_key else None
                if n is None:
                    if bk_part_id and bk_part_id.isdigit():
                        n = int(bk_part_id)
                if n is None:
                    last_numbers[it] = last_numbers.get(it, 0) + 1
                    n = last_numbers[it]
                else:
                    # Ensure counters won't collide with existing n
                    last_numbers[it] = max(last_numbers.get(it, 0), n)

                changed_fields: List[str] = []

                # Fill missing bk_part_id if blank
                if not bk_part_id:
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

                # Ensure bk_part_key is present and valid
                key_n = _extract_n_from_key(bk_part_key) if bk_part_key else None
                if key_n is None:
                    bk_part_key = f"BK-{it}-{n:08d}"
                    row["bk_part_key"] = bk_part_key
                    changed_fields.append("bk_part_key")

                # Record changes for audit + CSV write
                if changed_fields:
                    changes.append({
                        "action": "corrected_existing",
                        "bl_part_id": bl,
                        "item_type": it,
                        "bk_part_id": bk_part_id,
                        "brikick_name": brikick_name,
                        "api_item_type": api_item_type,
                        "bk_part_key": bk_part_key,
                        "note": "filled/normalized: " + ", ".join(changed_fields),
                    })
                    new_rows.append({**row})  # mark that CSV should be updated

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
            changes.append({
                "action": "created_new",
                "bl_part_id": bl,
                "item_type": it,
                "bk_part_id": bk_part_id,
                "brikick_name": brikick_name,
                "api_item_type": api_item_type,
                "bk_part_key": bk_part_key,
                "note": "auto-generated (not present in bk_mapping.csv)",
            })
            _upsert_db(con, bl, it, bk_part_id, brikick_name, api_item_type, bk_part_key)
            created += 1

        con.commit()

        if args.write_csv and new_rows:
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
            _write_csv_canonical(csv_path, header, csv_rows)

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
