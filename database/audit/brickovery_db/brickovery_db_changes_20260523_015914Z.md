# Brickovery DB backup & change audit — 20260523_015914Z

## Context
- created_at_utc: **20260523_015914Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2985` (id `26320343976`)
- commit: `72113e405fd160f5cd77a2b4c63826eb5658db5e`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `a0a3fe5219084f4ed224c7ae6d184d8d49d2fcab0bbd132b712b285cca96f192`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260523_015914Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260523_015914Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8bd5320055223104b48cabac4a8fad92df64ecbd17dad9e63a439b2b1c1b1710`
- csv_size_bytes (pre-update): `26312134`
- csv_backup_file: `brickovery_db_csv_backup_20260523_015914Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205929`
- items_db: `206452`
- items_missing_in_db: `23`
- codes_upstream: `84409`
- codes_db: `248115`
- codes_missing_in_db: `10`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260523_015914Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
