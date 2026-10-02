# Brickovery DB backup & change audit — 20261002_030026Z

## Context
- created_at_utc: **20261002_030026Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3562` (id `36957634631`)
- commit: `1d3e881d9937b1a253731dfa89064a998ba18729`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `e7c5dad136dcebd8710e2e2ae74c29c89f43dbe12c1b8eb342038e4d46764d87`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261002_030026Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261002_030026Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `519a54b116378c72525c578bbfe0714d8500f6d4c1c7a14e3b31d02e24579a9b`
- csv_size_bytes (pre-update): `26853336`
- csv_backup_file: `brickovery_db_csv_backup_20261002_030026Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211385`
- items_db: `213135`
- items_missing_in_db: `86`
- codes_upstream: `86746`
- codes_db: `257548`
- codes_missing_in_db: `8`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261002_030026Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
