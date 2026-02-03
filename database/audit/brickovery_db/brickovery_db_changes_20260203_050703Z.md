# Brickovery DB backup & change audit — 20260203_050703Z

## Context
- created_at_utc: **20260203_050703Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `76` (id `21617825827`)
- commit: `45fe3111660711c17277a10e61f1f42f055c5e40`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `eeae1c531a19d0ccfa16ccc26b71df589285dbb8b2dfe7d7b785e8661cf02e23`
- db_size_bytes (pre-update): `88240128`
- backup_file: `brickovery_db_backup_20260203_050703Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260203_050703Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e37e78e570442922a4ab580a6a3051e71e25851eb0139f1af3012f20d64f91d7`
- csv_size_bytes (pre-update): `16838071`
- csv_backup_file: `brickovery_db_csv_backup_20260203_050703Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202386`
- items_db: `237909`
- items_missing_in_db: `18`
- codes_upstream: `83275`
- codes_db: `282541`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260203_050703Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
