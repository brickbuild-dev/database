# Brickovery DB backup & change audit — 20260730_012227Z

## Context
- created_at_utc: **20260730_012227Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3186` (id `30505104603`)
- commit: `10cfe52fd0286ca5bae085d891bbb2e5b08649f2`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `badcb84b2a40361c1236335c3f27162f097b465eeae80b638f15cdfc9f11ab59`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260730_012227Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260730_012227Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `bcac021a7d79c768e8664a039b902890674b59bdc442fc106076f25ac53d431a`
- csv_size_bytes (pre-update): `26507318`
- csv_backup_file: `brickovery_db_csv_backup_20260730_012227Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `208186`
- items_db: `208861`
- items_missing_in_db: `52`
- codes_upstream: `85418`
- codes_db: `251511`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260730_012227Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
