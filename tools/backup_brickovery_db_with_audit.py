#!/usr/bin/env python3
"""
Immutable backup + audit for brickovery.db (Brikick critical data)

Requirements (user-specified)
- Every time the DB is going to be modified (delta apply or manual force rebuild),
  create a *new* backup file (never overwrite old backups).
- Create a detailed, append-only audit document that reports what changed / why.
- Both backup filename and audit filename MUST include UTC date+time, and the audit
  must repeat the timestamp inside the document for readability during incident response.

This script is intentionally side-effect limited:
- It does NOT modify the DB content.
- It only reads the DB file and optionally a context JSON (e.g., semantic check results),
  then writes backup + meta + audit files.

Outputs (default structure suggested for repo):
- database/backups/brickovery_db/brickovery_db_backup_YYYYMMDD_HHMMSSZ.sqlite.gz
- database/backups/brickovery_db/brickovery_db_backup_YYYYMMDD_HHMMSSZ.meta.json
- database/audit/brickovery_db/brickovery_db_changes_YYYYMMDD_HHMMSSZ.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import gzip
from pathlib import Path
from datetime import datetime, timezone


def _utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%SZ")


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _gzip_copy(src: Path, dst_gz: Path) -> None:
    dst_gz.parent.mkdir(parents=True, exist_ok=True)
    with src.open("rb") as f_in, gzip.open(dst_gz, "wb", compresslevel=9) as f_out:
        shutil.copyfileobj(f_in, f_out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True, help="Path to brickovery SQLite DB")
    ap.add_argument("--backup-dir", required=True, help="Directory to write immutable backups")
    ap.add_argument("--audit-dir", required=True, help="Directory to write immutable audit reports")
    ap.add_argument("--reason", required=True, help="Reason for backup (semantic_delta|manual_force_rebuild|...)")
    ap.add_argument("--context-json", default="", help="Optional JSON context (semantic check/apply output)")
    ap.add_argument("--also-backup-csv", default="", help="Optional path to brickovery_db.csv to snapshot too")
    args = ap.parse_args()

    db_path = Path(args.db)
    if not db_path.exists():
        print(f"[backup] DB not found: {db_path}", file=sys.stderr)
        return 2

    stamp = _utc_stamp()
    backup_dir = Path(args.backup_dir)
    audit_dir = Path(args.audit_dir)
    backup_dir.mkdir(parents=True, exist_ok=True)
    audit_dir.mkdir(parents=True, exist_ok=True)

    db_sha = _sha256_file(db_path)
    db_size = db_path.stat().st_size

    backup_gz = backup_dir / f"brickovery_db_backup_{stamp}.sqlite.gz"
    meta_json = backup_dir / f"brickovery_db_backup_{stamp}.meta.json"
    audit_md = audit_dir / f"brickovery_db_changes_{stamp}.md"

    # Guard: never overwrite
    for p in (backup_gz, meta_json, audit_md):
        if p.exists():
            print(f"[backup] Refusing to overwrite existing file: {p}", file=sys.stderr)
            return 3

    # Create gzip backup
    _gzip_copy(db_path, backup_gz)

    ctx = {}
    if args.context_json:
        cj = Path(args.context_json)
        if cj.exists():
            try:
                ctx = json.loads(cj.read_text(encoding="utf-8"))
            except Exception as e:
                ctx = {"_context_read_error": str(e), "_context_path": str(cj)}
        else:
            ctx = {"_context_missing": str(cj)}

    # Optional CSV snapshot (if requested and exists)
    csv_backup_gz = ""
    csv_sha = ""
    csv_size = 0
    if args.also_backup_csv:
        csv_path = Path(args.also_backup_csv)
        if csv_path.exists():
            csv_sha = _sha256_file(csv_path)
            csv_size = csv_path.stat().st_size
            csv_backup_gz_path = backup_dir / f"brickovery_db_csv_backup_{stamp}.csv.gz"
            if csv_backup_gz_path.exists():
                print(f"[backup] Refusing to overwrite existing file: {csv_backup_gz_path}", file=sys.stderr)
                return 3
            _gzip_copy(csv_path, csv_backup_gz_path)
            csv_backup_gz = str(csv_backup_gz_path)

    meta = {
        "created_at_utc": stamp,
        "reason": args.reason,
        "db_path": str(db_path),
        "db_sha256": db_sha,
        "db_size_bytes": db_size,
        "backup_file": str(backup_gz),
        "backup_file_format": "sqlite.gz",
        "context_json": args.context_json or "",
        "context": ctx,
    }
    if csv_backup_gz:
        meta.update(
            {
                "csv_path": args.also_backup_csv,
                "csv_sha256": csv_sha,
                "csv_size_bytes": csv_size,
                "csv_backup_file": csv_backup_gz,
            }
        )

    meta_json.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    # Human readable audit (append-only via unique filenames)
    gh = {
        "GITHUB_REPOSITORY": os.getenv("GITHUB_REPOSITORY", ""),
        "GITHUB_WORKFLOW": os.getenv("GITHUB_WORKFLOW", ""),
        "GITHUB_RUN_ID": os.getenv("GITHUB_RUN_ID", ""),
        "GITHUB_RUN_NUMBER": os.getenv("GITHUB_RUN_NUMBER", ""),
        "GITHUB_SHA": os.getenv("GITHUB_SHA", ""),
        "GITHUB_ACTOR": os.getenv("GITHUB_ACTOR", ""),
        "GITHUB_REF": os.getenv("GITHUB_REF", ""),
    }

    def _ctx_get(k, default=""):
        v = ctx.get(k, default) if isinstance(ctx, dict) else default
        return v

    audit_lines = []
    audit_lines.append(f"# Brickovery DB backup & change audit — {stamp}")
    audit_lines.append("")
    audit_lines.append("## Context")
    audit_lines.append(f"- created_at_utc: **{stamp}**")
    audit_lines.append(f"- reason: **{args.reason}**")
    audit_lines.append(f"- repository: `{gh['GITHUB_REPOSITORY']}`")
    audit_lines.append(f"- workflow: `{gh['GITHUB_WORKFLOW']}`")
    audit_lines.append(f"- run: `{gh['GITHUB_RUN_NUMBER']}` (id `{gh['GITHUB_RUN_ID']}`)")
    audit_lines.append(f"- commit: `{gh['GITHUB_SHA']}`")
    audit_lines.append(f"- actor: `{gh['GITHUB_ACTOR']}`")
    audit_lines.append(f"- ref: `{gh['GITHUB_REF']}`")
    audit_lines.append("")
    audit_lines.append("## Backup (immutable)")
    audit_lines.append(f"- db_path: `{db_path}`")
    audit_lines.append(f"- db_sha256 (pre-update): `{db_sha}`")
    audit_lines.append(f"- db_size_bytes (pre-update): `{db_size}`")
    audit_lines.append(f"- backup_file: `{backup_gz.name}`")
    audit_lines.append(f"- meta_file: `{meta_json.name}`")
    if csv_backup_gz:
        audit_lines.append("")
        audit_lines.append("## Optional CSV snapshot")
        audit_lines.append(f"- csv_sha256 (pre-update): `{csv_sha}`")
        audit_lines.append(f"- csv_size_bytes (pre-update): `{csv_size}`")
        audit_lines.append(f"- csv_backup_file: `{Path(csv_backup_gz).name}`")
    audit_lines.append("")
    audit_lines.append("## Intended change summary (from context JSON, if provided)")
    if ctx:
        # include the most relevant fields but avoid dumping huge blobs
        keys = [
            "semantic_new_data",
            "items_upstream", "items_db", "items_missing_in_db",
            "codes_upstream", "codes_db", "codes_missing_in_db",
            "db_inserted_items", "db_inserted_codes",
            "unknown_color_tokens_count",
        ]
        for k in keys:
            if k in ctx:
                audit_lines.append(f"- {k}: `{ctx.get(k)}`")
    else:
        audit_lines.append("- (no context JSON provided)")
    audit_lines.append("")
    audit_lines.append("## Restore procedure (emergency)")
    audit_lines.append("1) Stop any writers (workflows/scripts) that may modify the DB.")
    audit_lines.append(f"2) Download `database/backups/brickovery_db/{backup_gz.name}` and decompress it:")
    audit_lines.append("   - `gzip -d brickovery_db_backup_...sqlite.gz`")
    audit_lines.append("3) Replace `database/brickovery.db` with the decompressed file.")
    audit_lines.append("4) Re-run export (mode export) to regenerate CSV and issues.")
    audit_lines.append("")
    audit_lines.append("## Notes")
    audit_lines.append("- Backups and audit reports are immutable by design (new timestamped files per update).")
    audit_lines.append("- This DB is the Brikick critical dataset; treat backups as P0 artefacts.")

    audit_md.write_text("\n".join(audit_lines) + "\n", encoding="utf-8")

    # Print a short JSON to stdout (helpful for debugging / step logs)
    print(json.dumps(
        {
            "created_at_utc": stamp,
            "reason": args.reason,
            "db_sha256": db_sha,
            "backup_file": str(backup_gz),
            "meta_file": str(meta_json),
            "audit_file": str(audit_md),
        },
        ensure_ascii=False
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
