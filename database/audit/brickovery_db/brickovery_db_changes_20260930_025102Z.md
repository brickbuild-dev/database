# Brickovery DB backup & change audit — 20260930_025102Z

## Context
- created_at_utc: **20260930_025102Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3544` (id `36661182078`)
- commit: `85d631a3a659b67654547eb5e9610fba685dfd9c`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `519b654664d2275a88ed7196fdae8506ee5691b886ad8afec8d14575e3cda839`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260930_025102Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260930_025102Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d5187c870647717f1173508f98ce600c1abc997318c2b9689616ddfc536b8d65`
- csv_size_bytes (pre-update): `26774230`
- csv_backup_file: `brickovery_db_csv_backup_20260930_025102Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211271`
- items_db: `212169`
- items_missing_in_db: `938`
- codes_upstream: `86725`
- codes_db: `256198`
- codes_missing_in_db: `373`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260930_025102Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
