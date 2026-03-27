# Brickovery DB backup & change audit — 20260327_011430Z

## Context
- created_at_utc: **20260327_011430Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `417` (id `23626169381`)
- commit: `ee119b9bd12b7e5d1b682c34db1057350587e762`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `3a4be55a68e319f757f39e9c1c2830e8ca31a0f92d71a416fd6dfcb529024d2f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260327_011430Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260327_011430Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `0a32a92bef7a435d0f5a32a6d9b93c8650824255fcb17b14823da7013ba08818`
- csv_size_bytes (pre-update): `26112536`
- csv_backup_file: `brickovery_db_csv_backup_20260327_011430Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `204517`
- items_db: `204204`
- items_missing_in_db: `407`
- codes_upstream: `84066`
- codes_db: `244632`
- codes_missing_in_db: `12`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260327_011430Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
