# Brickovery DB backup & change audit — 20261028_025825Z

## Context
- created_at_utc: **20261028_025825Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3810` (id `40623277270`)
- commit: `b490cfdda5b852118613cab97dac23e7f16cad99`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `b6aad2ddf75e37b06af95cc4cd55acf270f87d8b802b90d3a163ef3c656a0d9c`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261028_025825Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261028_025825Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d6af69da9c0c9d3d6861fae8f9d2a68950beaa44c7edac7d0d0866c323681d10`
- csv_size_bytes (pre-update): `26905374`
- csv_backup_file: `brickovery_db_csv_backup_20261028_025825Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211856`
- items_db: `213709`
- items_missing_in_db: `23`
- codes_upstream: `87070`
- codes_db: `258446`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261028_025825Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
