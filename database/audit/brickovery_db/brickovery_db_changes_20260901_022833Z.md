# Brickovery DB backup & change audit — 20260901_022833Z

## Context
- created_at_utc: **20260901_022833Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3252` (id `33462263798`)
- commit: `72123354577e74c39aa52a6300e00aa7daa0219f`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `494e89941b81f41add5124f93f78748c6ebe2fe7fbf389c6c3ef541760a89269`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260901_022833Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260901_022833Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `4e191093845f14b3b09ff461383e7e62d5e743ccf0dcc10d3622117d67aa9c30`
- csv_size_bytes (pre-update): `26671868`
- csv_backup_file: `brickovery_db_csv_backup_20260901_022833Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209925`
- items_db: `210739`
- items_missing_in_db: `6`
- codes_upstream: `86354`
- codes_db: `254392`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260901_022833Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
