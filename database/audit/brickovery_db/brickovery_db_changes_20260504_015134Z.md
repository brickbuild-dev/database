# Brickovery DB backup & change audit — 20260504_015134Z

## Context
- created_at_utc: **20260504_015134Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2951` (id `25297062965`)
- commit: `f062e364f7e0c50fcbfb466656edbbec2ccf67f3`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `c6c2cac68524776efaa2a2ee50415ac1b4b1b1e4e030e1500b9583733cf02e1e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260504_015134Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260504_015134Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e326ac5a53744cd3ad98accf4b2a926b1bbedd20996c3ba590e9b71f42877794`
- csv_size_bytes (pre-update): `26249998`
- csv_backup_file: `brickovery_db_csv_backup_20260504_015134Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205650`
- items_db: `205979`
- items_missing_in_db: `69`
- codes_upstream: `84733`
- codes_db: `247036`
- codes_missing_in_db: `59`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260504_015134Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
