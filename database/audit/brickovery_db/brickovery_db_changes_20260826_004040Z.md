# Brickovery DB backup & change audit — 20260826_004040Z

## Context
- created_at_utc: **20260826_004040Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3240` (id `32915602214`)
- commit: `ee2127349e6c2a1489de519885d2dd806a174686`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `a692cc0756cdb9507e536567031bc6fead8f7593f3ddcfcc675b4f4f76d17e65`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260826_004040Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260826_004040Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `9eefe2eae1dd2ed982a533925a73cd5990ed0f1412673e0d8a1319ffaa651c42`
- csv_size_bytes (pre-update): `26660969`
- csv_backup_file: `brickovery_db_csv_backup_20260826_004040Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209840`
- items_db: `210625`
- items_missing_in_db: `25`
- codes_upstream: `86341`
- codes_db: `254207`
- codes_missing_in_db: `22`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260826_004040Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
