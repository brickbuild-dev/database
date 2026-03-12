# Brickovery DB backup & change audit — 20260312_005926Z

## Context
- created_at_utc: **20260312_005926Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `387` (id `22981774397`)
- commit: `cf5fef25b6594de031d698cf5e460d2da98cd7de`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `e0a0aa7229228d4033b8dd2fa6687a11cfe5386e83ade4070039e0f5807abf08`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260312_005926Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260312_005926Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `bc8d2f230688a62856cee93db9aec626ad0dee85a6e860a0288968b92e56f425`
- csv_size_bytes (pre-update): `26068645`
- csv_backup_file: `brickovery_db_csv_backup_20260312_005926Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203467`
- items_db: `203521`
- items_missing_in_db: `13`
- codes_upstream: `83938`
- codes_db: `243837`
- codes_missing_in_db: `3`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260312_005926Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
