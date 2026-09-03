# Brickovery DB backup & change audit — 20260903_015803Z

## Context
- created_at_utc: **20260903_015803Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3256` (id `33705161504`)
- commit: `3d983821084fba60a7740667b589d6c4f996112e`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `b5da06d4dd6e0c3f7762ff3bd0cf9cef0d46382604bde1311f97b9a67716e219`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260903_015803Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260903_015803Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `7b9a0c4172b46518092fc4711bc173d141c912c1021f961e5366738da615b7c4`
- csv_size_bytes (pre-update): `26684760`
- csv_backup_file: `brickovery_db_csv_backup_20260903_015803Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210202`
- items_db: `210950`
- items_missing_in_db: `73`
- codes_upstream: `86392`
- codes_db: `254610`
- codes_missing_in_db: `26`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260903_015803Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
