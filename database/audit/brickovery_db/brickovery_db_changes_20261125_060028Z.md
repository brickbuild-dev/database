# Brickovery DB backup & change audit — 20261125_060028Z

## Context
- created_at_utc: **20261125_060028Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3885` (id `45556672692`)
- commit: `998f8328b661a768c08e5c43cd5040a3747e2cfa`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `ba9e69d40edb1223f415c00ca8782c6bd1bfc196f27fa38c627461083183da5c`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261125_060028Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261125_060028Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `5817449fa7fa4b36b6c8595b3185f8865f01da2ea366583a790b6f5bb56c2193`
- csv_size_bytes (pre-update): `26932071`
- csv_backup_file: `brickovery_db_csv_backup_20261125_060028Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212177`
- items_db: `214053`
- items_missing_in_db: `9`
- codes_upstream: `87191`
- codes_db: `258911`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261125_060028Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
