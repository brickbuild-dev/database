# Brickovery DB backup & change audit — 20260424_012856Z

## Context
- created_at_utc: **20260424_012856Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2930` (id `24867395363`)
- commit: `1a2077a51e6d122cc2c3dd747e7d368c66403418`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `a4cef9876f6fb5f2a82d347677428f4a03c007cdeba0249ba6cfe8b046233ebd`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260424_012856Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260424_012856Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `467a08a55f3b794eaa69ad795a1fbf2250d4806d4eb164bd1026eed8676dee61`
- csv_size_bytes (pre-update): `26201234`
- csv_backup_file: `brickovery_db_csv_backup_20260424_012856Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205282`
- items_db: `205646`
- items_missing_in_db: `3`
- codes_upstream: `84246`
- codes_db: `246194`
- codes_missing_in_db: `75`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260424_012856Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
