# Brickovery DB backup & change audit — 20260416_012816Z

## Context
- created_at_utc: **20260416_012816Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2894` (id `24486937493`)
- commit: `05de597b30ef8cd44e9c5d74431593544841f6c9`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `bce854a0e84f90f2be57cccf58663ec7349cd71502bcef5b3aca3a85b1d4279a`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260416_012816Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260416_012816Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e3faf5464602fa473761739d480b0861835762c32dfd673530903aa9b86411f5`
- csv_size_bytes (pre-update): `26194056`
- csv_backup_file: `brickovery_db_csv_backup_20260416_012816Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205205`
- items_db: `205549`
- items_missing_in_db: `4`
- codes_upstream: `84160`
- codes_db: `246068`
- codes_missing_in_db: `4`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260416_012816Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
