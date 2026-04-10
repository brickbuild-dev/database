# Brickovery DB backup & change audit — 20260410_012119Z

## Context
- created_at_utc: **20260410_012119Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2799` (id `24221464516`)
- commit: `4eff5c0452faa239b59a52202fc5f8d09d659b44`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `b3420d1be841d7e08a205ebd4cc729ac5fada63891fe16d2373d0f84e3442327`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260410_012119Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260410_012119Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `b9c25d1c77ce6471b71566dbccd900120bd01f6470919a8df51ab2bd3d597eb5`
- csv_size_bytes (pre-update): `26153033`
- csv_backup_file: `brickovery_db_csv_backup_20260410_012119Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205150`
- items_db: `204908`
- items_missing_in_db: `576`
- codes_upstream: `84124`
- codes_db: `245350`
- codes_missing_in_db: `54`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260410_012119Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
