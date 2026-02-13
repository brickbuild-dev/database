# Brickovery DB backup & change audit — 20260213_051358Z

## Context
- created_at_utc: **20260213_051358Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `340` (id `21975553420`)
- commit: `f4356fdda9063ecb41d96d1b65a409c5a69516a3`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `890e8b23392499ecf2b27144df606553e9e74f9b48160b66c5576017f280907e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260213_051358Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260213_051358Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `2d27c94466274c9b88c9dca57219c8b15e4489f387c0981ca28589599569a0d4`
- csv_size_bytes (pre-update): `25973821`
- csv_backup_file: `brickovery_db_csv_backup_20260213_051358Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202469`
- items_db: `202464`
- items_missing_in_db: `9`
- codes_upstream: `83315`
- codes_db: `242186`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260213_051358Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
