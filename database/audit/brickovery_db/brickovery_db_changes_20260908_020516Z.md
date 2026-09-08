# Brickovery DB backup & change audit — 20260908_020516Z

## Context
- created_at_utc: **20260908_020516Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3354` (id `34178392026`)
- commit: `13b36c7f7b9221b6e1642ba2e38effdffd6b18eb`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `0bc1fb3e712a0deb65e6b8d0a0773e40b135be6a236803c2c28093fb3bd11e2b`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260908_020516Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260908_020516Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `814868f63ebd8adbd2cf9cf465ae2841582b44a780eac5a7b55fce3e6f0197f1`
- csv_size_bytes (pre-update): `26713108`
- csv_backup_file: `brickovery_db_csv_backup_20260908_020516Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210458`
- items_db: `211288`
- items_missing_in_db: `10`
- codes_upstream: `86528`
- codes_db: `255096`
- codes_missing_in_db: `9`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260908_020516Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
