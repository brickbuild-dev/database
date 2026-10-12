# Brickovery DB backup & change audit — 20261012_030519Z

## Context
- created_at_utc: **20261012_030519Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3668` (id `38197975092`)
- commit: `7c30a63c59e1efb84ff97f51b1c52d93c5d9e85f`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `5d75cc209521c4ed4a3d777439bcdef72ec4fce7dbacd9860a238f27a653c94f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261012_030519Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261012_030519Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `817f00f1223446f0264447ee4b923d97660defaef24ae3d3c91f00b3998d4a22`
- csv_size_bytes (pre-update): `26882599`
- csv_backup_file: `brickovery_db_csv_backup_20261012_030519Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211586`
- items_db: `213425`
- items_missing_in_db: `14`
- codes_upstream: `86968`
- codes_db: `258050`
- codes_missing_in_db: `13`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261012_030519Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
