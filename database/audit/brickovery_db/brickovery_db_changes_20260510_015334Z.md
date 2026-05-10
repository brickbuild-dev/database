# Brickovery DB backup & change audit — 20260510_015334Z

## Context
- created_at_utc: **20260510_015334Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2963` (id `25616916241`)
- commit: `cfd88e4a55d8ff9a40772d847db84e2e509363ea`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `93bf9f918f2155fb4135413b705ac3ecf008d1579b7873f8e3f3f1d3d3024148`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260510_015334Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260510_015334Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `dd1caebad39ef3bc3d6b2fe7176afed7b7a80da61278b570ee09d3142da7bd28`
- csv_size_bytes (pre-update): `26282207`
- csv_backup_file: `brickovery_db_csv_backup_20260510_015334Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205741`
- items_db: `206164`
- items_missing_in_db: `23`
- codes_upstream: `84225`
- codes_db: `247592`
- codes_missing_in_db: `22`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260510_015334Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
