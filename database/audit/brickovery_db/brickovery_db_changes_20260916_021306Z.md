# Brickovery DB backup & change audit — 20260916_021306Z

## Context
- created_at_utc: **20260916_021306Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3388` (id `35046485607`)
- commit: `a4b7f4c098035452f4491650a476c7ae654512cd`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `041677c6d88851607ed14158eff78014168dfa5010546542920b15a72708e3f6`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260916_021306Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260916_021306Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `eedb6dfa064455b303d9f8c4988b5c5c52a25d9f46f05479b98843e95bce7465`
- csv_size_bytes (pre-update): `26741171`
- csv_backup_file: `brickovery_db_csv_backup_20260916_021306Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210776`
- items_db: `211618`
- items_missing_in_db: `25`
- codes_upstream: `86685`
- codes_db: `255585`
- codes_missing_in_db: `20`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260916_021306Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
