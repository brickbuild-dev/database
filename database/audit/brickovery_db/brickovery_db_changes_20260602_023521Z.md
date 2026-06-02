# Brickovery DB backup & change audit — 20260602_023521Z

## Context
- created_at_utc: **20260602_023521Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3005` (id `26794638748`)
- commit: `0fecb919b18ca275f1aa9945711dd8d06a8d0ea2`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `aaf8dbb381a2652d5ae91b0fae745ff0c68c31323e049392e03c0f00dfa91ccb`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260602_023521Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260602_023521Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e9ca066dff1801bdb86ee37bab45f629097626a24e6fd3528b57509604f9c7df`
- csv_size_bytes (pre-update): `26325699`
- csv_backup_file: `brickovery_db_csv_backup_20260602_023521Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206464`
- items_db: `206682`
- items_missing_in_db: `367`
- codes_upstream: `84426`
- codes_db: `248356`
- codes_missing_in_db: `16`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260602_023521Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
