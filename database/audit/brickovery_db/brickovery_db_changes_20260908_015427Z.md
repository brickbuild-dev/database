# Brickovery DB backup & change audit — 20260908_015427Z

## Context
- created_at_utc: **20260908_015427Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3353` (id `34177795703`)
- commit: `b115cdee785888370bc22da8c16111504cf545c2`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `4ceb2332e681b80ecb3623062620766452c9eca2bcf3f33157b21b6338db2c06`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260908_015427Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260908_015427Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `469603c77d70c9f96fe88475b120ef520ddf45c273dd965f41d1ead91b9239ec`
- csv_size_bytes (pre-update): `26703459`
- csv_backup_file: `brickovery_db_csv_backup_20260908_015427Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210448`
- items_db: `211184`
- items_missing_in_db: `104`
- codes_upstream: `86519`
- codes_db: `254931`
- codes_missing_in_db: `61`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260908_015427Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
