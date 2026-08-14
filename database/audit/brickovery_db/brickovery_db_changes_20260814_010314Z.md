# Brickovery DB backup & change audit — 20260814_010314Z

## Context
- created_at_utc: **20260814_010314Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3216` (id `31758999948`)
- commit: `5b9c2dae7fd47f1ce396c942962930a6bd2bd4ce`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `c3a8d2038a017521acb843d6d855063660cb367e70c83b062c2e4fb7f9fd67ef`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260814_010314Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260814_010314Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `84c60cd528e8b02e100a94fb1e6e9072406cae49eff3dc844c936518065821e9`
- csv_size_bytes (pre-update): `26632323`
- csv_backup_file: `brickovery_db_csv_backup_20260814_010314Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209557`
- items_db: `210334`
- items_missing_in_db: `3`
- codes_upstream: `86145`
- codes_db: `253716`
- codes_missing_in_db: `18`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260814_010314Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
