# Brickovery DB backup & change audit — 20261005_025219Z

## Context
- created_at_utc: **20261005_025219Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3654` (id `37256585517`)
- commit: `789ecaf725dbeddf429bc4ad4089d1656cbea3e1`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `6a147a9708878fdbe5cfe4b64e92871efa7d330a457b7b3e1e014be197464b3f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261005_025219Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261005_025219Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `bab8ba41c8c5f6e8a7e12ef953dc9ae98d52472d1fc8e5e68916f84878c9adba`
- csv_size_bytes (pre-update): `26863663`
- csv_backup_file: `brickovery_db_csv_backup_20261005_025219Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211453`
- items_db: `213270`
- items_missing_in_db: `24`
- codes_upstream: `86823`
- codes_db: `257725`
- codes_missing_in_db: `37`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261005_025219Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
