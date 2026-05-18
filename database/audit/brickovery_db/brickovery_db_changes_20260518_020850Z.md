# Brickovery DB backup & change audit — 20260518_020850Z

## Context
- created_at_utc: **20260518_020850Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2975` (id `26009629120`)
- commit: `759d1bd6c9d5457aa0f2bd8599b0bae5e2249ea1`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `5180b9e450394075cb67b1d507402dfb41ac5fb6f62c8373b3a93fe475e40a4a`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260518_020850Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260518_020850Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `1c80b881eedf7401a4d80d15d4feaa9dac1ea5fa88921a8e5cc5c31af54cab54`
- csv_size_bytes (pre-update): `26300833`
- csv_backup_file: `brickovery_db_csv_backup_20260518_020850Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205869`
- items_db: `206334`
- items_missing_in_db: `23`
- codes_upstream: `84370`
- codes_db: `247913`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260518_020850Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
