# Brickovery DB backup & change audit — 20260502_013356Z

## Context
- created_at_utc: **20260502_013356Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2947` (id `25240363011`)
- commit: `cfa17523fc980be8a01a586c2f70ea59172b7a9e`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `88200d815a3e57bda8621185510399644cdd57ffd2e130252775074bc566dda3`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260502_013356Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260502_013356Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `b300e6e8a2438f49b305cb6c80d8b82988d4c29166c854ddc9fdc09fb913d641`
- csv_size_bytes (pre-update): `26224778`
- csv_backup_file: `brickovery_db_csv_backup_20260502_013356Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205532`
- items_db: `205767`
- items_missing_in_db: `139`
- codes_upstream: `84517`
- codes_db: `246602`
- codes_missing_in_db: `54`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260502_013356Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
