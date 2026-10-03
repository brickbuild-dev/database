# Brickovery DB backup & change audit — 20261003_024633Z

## Context
- created_at_utc: **20261003_024633Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3650` (id `37090528375`)
- commit: `02187db81a633aec4108ea1561156351ea6d5d25`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `7569d2c39580a770b0f795480f13449e3da1dc5051e1ef2a81f48f2914ca8716`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261003_024633Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261003_024633Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `02b8e03c67b5b8d189fb9469036eb8d92c41fd664a93ce86c6030d132916798b`
- csv_size_bytes (pre-update): `26859681`
- csv_backup_file: `brickovery_db_csv_backup_20261003_024633Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211401`
- items_db: `213236`
- items_missing_in_db: `1`
- codes_upstream: `86749`
- codes_db: `257657`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261003_024633Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
