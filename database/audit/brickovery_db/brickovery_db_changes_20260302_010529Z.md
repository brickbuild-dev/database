# Brickovery DB backup & change audit — 20260302_010529Z

## Context
- created_at_utc: **20260302_010529Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `367` (id `22557251327`)
- commit: `467527aa9a15742c286969ea3734510178cde71b`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `9421804b3ae5dc3992a30d1907e5c22338d67a55fe4f99bee859f3fc4b56b08f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260302_010529Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260302_010529Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `2cced9334fef0473c61d2c41bbc4da15581459c56a6c0a856d4213625a3c6661`
- csv_size_bytes (pre-update): `26025908`
- csv_backup_file: `brickovery_db_csv_backup_20260302_010529Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203221`
- items_db: `203045`
- items_missing_in_db: `223`
- codes_upstream: `83725`
- codes_db: `243105`
- codes_missing_in_db: `71`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260302_010529Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
