# Brickovery DB backup & change audit — 20260626_021206Z

## Context
- created_at_utc: **20260626_021206Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3093` (id `28212502855`)
- commit: `cada6665a74c1af5102c6e30e5d76add38e17906`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `6bd353c5dc40307d39c33e24ea23fc0911957f39f7984a4e2baff14d0fa3213e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260626_021206Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260626_021206Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d3cf64eccd314ca2ecea8d259378aa1aebaff1a4b56696c062fb5cce2c4a7481`
- csv_size_bytes (pre-update): `26438979`
- csv_backup_file: `brickovery_db_csv_backup_20260626_021206Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207520`
- items_db: `208109`
- items_missing_in_db: `73`
- codes_upstream: `85027`
- codes_db: `250317`
- codes_missing_in_db: `62`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260626_021206Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
