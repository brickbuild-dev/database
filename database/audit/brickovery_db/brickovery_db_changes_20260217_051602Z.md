# Brickovery DB backup & change audit — 20260217_051602Z

## Context
- created_at_utc: **20260217_051602Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `348` (id `22086786221`)
- commit: `b35c0a2edd7091f9c313349344885fe81a442566`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `380241427a44ddf55614b9e474f375eda92645f484d91df7fa20db1e9dde4622`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260217_051602Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260217_051602Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `050dae0a4e7c9d80fcd90e3185aae1cb4b58e46ced18eb044eff6fdf3449d06f`
- csv_size_bytes (pre-update): `25977068`
- csv_backup_file: `brickovery_db_csv_backup_20260217_051602Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202522`
- items_db: `202500`
- items_missing_in_db: `29`
- codes_upstream: `83430`
- codes_db: `242242`
- codes_missing_in_db: `93`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260217_051602Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
