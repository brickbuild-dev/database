# Brickovery DB backup & change audit — 20261126_055239Z

## Context
- created_at_utc: **20261126_055239Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3887` (id `45763562135`)
- commit: `d2a60efc3c02c9d65df1bd23ef9a310d201e6e0e`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `d41a15a9e24deeaca23c34c805364166cd1bdf421e24f2bcdaef2960ea6f5c7f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261126_055239Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261126_055239Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `dd1021a4b3265a4a03e641e5e5e078fc7a9d577698ee1f56c38e687f95b30062`
- csv_size_bytes (pre-update): `26932623`
- csv_backup_file: `brickovery_db_csv_backup_20261126_055239Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212192`
- items_db: `214062`
- items_missing_in_db: `15`
- codes_upstream: `87198`
- codes_db: `258920`
- codes_missing_in_db: `7`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261126_055239Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
