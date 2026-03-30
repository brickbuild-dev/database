# Brickovery DB backup & change audit — 20260330_011820Z

## Context
- created_at_utc: **20260330_011820Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `439` (id `23723803068`)
- commit: `d0a46e9749e3f2c343db9f8312c790bfa60245b5`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `214a4793b841719f725bb45c04632dd3bc7fdf5e1e97fbb074372b48cd35d8c8`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260330_011820Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260330_011820Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `4ff2adfddedbac1d2986f4e4afb9d3e85167374db9b41891dd828c5d4d841e7d`
- csv_size_bytes (pre-update): `26150246`
- csv_backup_file: `brickovery_db_csv_backup_20260330_011820Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `204583`
- items_db: `204859`
- items_missing_in_db: `49`
- codes_upstream: `84069`
- codes_db: `245299`
- codes_missing_in_db: `3`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260330_011820Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
