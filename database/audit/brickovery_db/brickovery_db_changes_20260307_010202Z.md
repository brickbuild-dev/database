# Brickovery DB backup & change audit — 20260307_010202Z

## Context
- created_at_utc: **20260307_010202Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `377` (id `22788392874`)
- commit: `dc5fe277b9dd85b7cef3a26ba84ab45dfa3bc69a`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `9c1c926aaa8c545309e59701b6cec672b6763d2a8845e019c3b7a4c88b1eb08b`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260307_010202Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260307_010202Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d29622351d314e140cd6363cc531b859b929f3185e37f619f27aa496a61d8f6e`
- csv_size_bytes (pre-update): `26053615`
- csv_backup_file: `brickovery_db_csv_backup_20260307_010202Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203348`
- items_db: `203377`
- items_missing_in_db: `25`
- codes_upstream: `83833`
- codes_db: `243576`
- codes_missing_in_db: `27`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260307_010202Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
