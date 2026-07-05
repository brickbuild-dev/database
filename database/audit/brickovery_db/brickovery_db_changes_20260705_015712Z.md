# Brickovery DB backup & change audit — 20260705_015712Z

## Context
- created_at_utc: **20260705_015712Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3110` (id `28726138735`)
- commit: `b2ef0818ad7cdf3060a6922ac4812f44a3380467`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `65abae1193cb14d61565261c7acc9fa5e075457f89e7b9eef4e1a698ce0d77e1`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260705_015712Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260705_015712Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8f2100dcc027bca98844ac2b5ee928960cd61096329536dd78a5684fd9f0f7d8`
- csv_size_bytes (pre-update): `26467852`
- csv_backup_file: `brickovery_db_csv_backup_20260705_015712Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207722`
- items_db: `208380`
- items_missing_in_db: `20`
- codes_upstream: `85204`
- codes_db: `250813`
- codes_missing_in_db: `10`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260705_015712Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
