# Brickovery DB backup & change audit — 20260824_004011Z

## Context
- created_at_utc: **20260824_004011Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3236` (id `32677038786`)
- commit: `25f457980b41a9b5900540fc7ca1c5b606913a3d`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `03c67b6fee7e03576c4c8bfa18987851491ea5f49f1e61efe83fbc3d89d44e41`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260824_004011Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260824_004011Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8cce1ff9345eb498bf3408952f459e08081567989125b74d0644655b15b56934`
- csv_size_bytes (pre-update): `26656864`
- csv_backup_file: `brickovery_db_csv_backup_20260824_004011Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209789`
- items_db: `210577`
- items_missing_in_db: `10`
- codes_upstream: `86311`
- codes_db: `254136`
- codes_missing_in_db: `8`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260824_004011Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
