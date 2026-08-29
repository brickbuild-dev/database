# Brickovery DB backup & change audit — 20260829_044054Z

## Context
- created_at_utc: **20260829_044054Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3246` (id `33234134010`)
- commit: `6b879639b1b32bde20e3154a390de3c0098bc1ab`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `e7fde9a06ea03ea59d9c103386868c6ef5aa17e9d2bd5922be415700fb0fc80d`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260829_044054Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260829_044054Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `732cb07f7b42d91b72b2eb29a069b3f9ce5ae0f3548a157f5e03310740c783e5`
- csv_size_bytes (pre-update): `26668518`
- csv_backup_file: `brickovery_db_csv_backup_20260829_044054Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209892`
- items_db: `210704`
- items_missing_in_db: `7`
- codes_upstream: `86345`
- codes_db: `254334`
- codes_missing_in_db: `19`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260829_044054Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
