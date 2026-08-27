# Brickovery DB backup & change audit — 20260827_053410Z

## Context
- created_at_utc: **20260827_053410Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3242` (id `33042552896`)
- commit: `7514b37775bc8fee1a7365196292b0caa0445729`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `1c910388dc39c2543ce7fd7cf5fec88175adb42d8cab75ba4ddb0927250bc28f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260827_053410Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260827_053410Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `a167fbd3d36b8bf25d23a347094940067adf7944e4e6aa98fb5a4a4dd3c99295`
- csv_size_bytes (pre-update): `26663617`
- csv_backup_file: `brickovery_db_csv_backup_20260827_053410Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209876`
- items_db: `210650`
- items_missing_in_db: `41`
- codes_upstream: `86364`
- codes_db: `254253`
- codes_missing_in_db: `27`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260827_053410Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
