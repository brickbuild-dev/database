# Brickovery DB backup & change audit — 20260321_010232Z

## Context
- created_at_utc: **20260321_010232Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `405` (id `23368584509`)
- commit: `806406d5738c4ed9773346fb8079360aa7c75390`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `87a7474024fb5aebc5d5aed158a73ba5a66c62f092c13c7335dce6c62b6a5b5e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260321_010232Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260321_010232Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `b16b3c927ffb71087371789c123c011e58d7811e252debe1d1a76577b5bb889f`
- csv_size_bytes (pre-update): `26088555`
- csv_backup_file: `brickovery_db_csv_backup_20260321_010232Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203717`
- items_db: `203775`
- items_missing_in_db: `23`
- codes_upstream: `84044`
- codes_db: `244182`
- codes_missing_in_db: `8`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260321_010232Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
