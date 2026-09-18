# Brickovery DB backup & change audit — 20260918_020154Z

## Context
- created_at_utc: **20260918_020154Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3392` (id `35297196052`)
- commit: `50abf9fe5063e5659b2d93defadbbc2ffe6cf797`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `24f6a58260fc3afb7e3e0f5454e983b48b68f9971210d90f9995eeb937c0b271`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260918_020154Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260918_020154Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `658e00e99a83b795e624bc59b188328011bb5935d02698d1b845456f303219ea`
- csv_size_bytes (pre-update): `26744350`
- csv_backup_file: `brickovery_db_csv_backup_20260918_020154Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210785`
- items_db: `211647`
- items_missing_in_db: `6`
- codes_upstream: `86688`
- codes_db: `255638`
- codes_missing_in_db: `4`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260918_020154Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
