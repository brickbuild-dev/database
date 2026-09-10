# Brickovery DB backup & change audit — 20260910_015526Z

## Context
- created_at_utc: **20260910_015526Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3364` (id `34426991809`)
- commit: `7ff27c65fce85ce3caf81edbb70dc287d0de19d8`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `fe3c428fb0c7157e69c01fccba75da4139b69b847563d6cc72b1f202e4265d4f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260910_015526Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260910_015526Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `c010ea77b3eaea90b87616ac20b5cac1947dacd4f5c683b934e96dd9df62b55f`
- csv_size_bytes (pre-update): `26720693`
- csv_backup_file: `brickovery_db_csv_backup_20260910_015526Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210623`
- items_db: `211361`
- items_missing_in_db: `114`
- codes_upstream: `86606`
- codes_db: `255227`
- codes_missing_in_db: `41`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260910_015526Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
