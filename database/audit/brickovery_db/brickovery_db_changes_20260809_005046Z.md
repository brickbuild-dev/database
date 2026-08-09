# Brickovery DB backup & change audit — 20260809_005046Z

## Context
- created_at_utc: **20260809_005046Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3206` (id `31286868076`)
- commit: `233546aaa084e098bc7ce88b3d140cd126385973`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `b5a72873f1f2fc98984522d607352cabfa2df2fd1c8b0d51f32b44943bec5df4`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260809_005046Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260809_005046Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `c7177173afb75e5ebffa8a29de0f3919815564861e98bd6bbed27c6335db364b`
- csv_size_bytes (pre-update): `26611484`
- csv_backup_file: `brickovery_db_csv_backup_20260809_005046Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209329`
- items_db: `210082`
- items_missing_in_db: `21`
- codes_upstream: `86014`
- codes_db: `253354`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260809_005046Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
