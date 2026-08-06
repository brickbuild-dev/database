# Brickovery DB backup & change audit — 20260806_012645Z

## Context
- created_at_utc: **20260806_012645Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3200` (id `31062398307`)
- commit: `03b10c8e056536b1ac3ac32b57e90cf7f4aedb75`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `5312ba3ad4c6018e74bfe23c76faf6cca724c778759e7592541cdad129e57107`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260806_012645Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260806_012645Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d726024741967185eea40e5dc6845967403e23cc935e356ffdef5eead7e2ee2b`
- csv_size_bytes (pre-update): `26598709`
- csv_backup_file: `brickovery_db_csv_backup_20260806_012645Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209234`
- items_db: `209890`
- items_missing_in_db: `117`
- codes_upstream: `86015`
- codes_db: `253126`
- codes_missing_in_db: `5`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260806_012645Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
