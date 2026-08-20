# Brickovery DB backup & change audit — 20260820_003944Z

## Context
- created_at_utc: **20260820_003944Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3228` (id `32317674056`)
- commit: `632fbf968eb4d8d2b2d25459eb0e14db6ed557f9`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `b158cea30766c9a8f4b29be9426c706419ccea38bd65f8571bf7ee7a1672514a`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260820_003944Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260820_003944Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `b6444d1d34e8b01b4595ff5814e158ef8ca952fa74d8d4272001d26dff701f6c`
- csv_size_bytes (pre-update): `26645784`
- csv_backup_file: `brickovery_db_csv_backup_20260820_003944Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209674`
- items_db: `210462`
- items_missing_in_db: `2`
- codes_upstream: `86234`
- codes_db: `253947`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260820_003944Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
