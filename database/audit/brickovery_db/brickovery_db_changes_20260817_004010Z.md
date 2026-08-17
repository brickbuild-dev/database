# Brickovery DB backup & change audit — 20260817_004010Z

## Context
- created_at_utc: **20260817_004010Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3222` (id `31982316109`)
- commit: `69ef39d7040690a6ca5b0369fddd8f1a8b70d047`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `ebb78054db60b3869e4ad183353ec0aefb8ecc85074098f998f7efa5eb5cba3e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260817_004010Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260817_004010Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `42fd53355bc9589e14ded1d7a9c64967acf1604adf3470dbf62874d31f893b7c`
- csv_size_bytes (pre-update): `26641484`
- csv_backup_file: `brickovery_db_csv_backup_20260817_004010Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209667`
- items_db: `210422`
- items_missing_in_db: `31`
- codes_upstream: `86234`
- codes_db: `253873`
- codes_missing_in_db: `31`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260817_004010Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
