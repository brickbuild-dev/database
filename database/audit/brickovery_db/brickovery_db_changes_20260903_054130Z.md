# Brickovery DB backup & change audit — 20260903_054130Z

## Context
- created_at_utc: **20260903_054130Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3281` (id `33719436584`)
- commit: `ae367caad6b1b49c0f8a854bc0e29e46e367c91d`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `0165c8c9fb5b67d396547efeaf9ebf017102dfaecda3d9a35c2806944a0788a4`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260903_054130Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260903_054130Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `058b8fccb6f2900f4c48d268c15a3b63f59a6c941f1d1b6c25831eb4eea2b01f`
- csv_size_bytes (pre-update): `26690486`
- csv_backup_file: `brickovery_db_csv_backup_20260903_054130Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210204`
- items_db: `211023`
- items_missing_in_db: `2`
- codes_upstream: `86394`
- codes_db: `254708`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260903_054130Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
