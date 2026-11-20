# Brickovery DB backup & change audit — 20261120_044857Z

## Context
- created_at_utc: **20261120_044857Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3879` (id `44675918545`)
- commit: `3245e546a8a988aeeb97ad11dff04268eaff254b`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `f688f788cb1fb49e45b441f4f41456d18bbd9c105667237675016aa50b1b8bad`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261120_044857Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261120_044857Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `611a25a02fd5a36be0c43b85b626e6a40a0cc8e8fcbb36bafd13acaec80e1c29`
- csv_size_bytes (pre-update): `26931916`
- csv_backup_file: `brickovery_db_csv_backup_20261120_044857Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212168`
- items_db: `214050`
- items_missing_in_db: `3`
- codes_upstream: `87191`
- codes_db: `258908`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261120_044857Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
