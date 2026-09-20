# Brickovery DB backup & change audit — 20260920_020938Z

## Context
- created_at_utc: **20260920_020938Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3396` (id `35482953168`)
- commit: `9c780c7fff1c1f9bc08ea1d6efe3c43b13f6e7fe`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `743e4922f9c479344cfe7607b2fd71643bbd5f95efa546bd0c301d9d3398a10f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260920_020938Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260920_020938Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `4410310764e220b6dd554d5f512ac5ac782d3e5e2473f3aa5af573496aaf7a17`
- csv_size_bytes (pre-update): `26746001`
- csv_backup_file: `brickovery_db_csv_backup_20260920_020938Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210830`
- items_db: `211656`
- items_missing_in_db: `42`
- codes_upstream: `86703`
- codes_db: `255666`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260920_020938Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
