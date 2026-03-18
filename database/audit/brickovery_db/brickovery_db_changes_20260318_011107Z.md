# Brickovery DB backup & change audit — 20260318_011107Z

## Context
- created_at_utc: **20260318_011107Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `399` (id `23224166273`)
- commit: `77b9451569233df92155db872e3335bff91f1aa1`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `599c2e4a6f5389433aef87725a5a1dfd6ef9fcccd556f0d84ca233f4cb16e9bf`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260318_011107Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260318_011107Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `3b5c963c64f1577cf28e175000eb5417faeb19c9a09c40af56c0290ab4f48733`
- csv_size_bytes (pre-update): `26082465`
- csv_backup_file: `brickovery_db_csv_backup_20260318_011107Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203672`
- items_db: `203704`
- items_missing_in_db: `42`
- codes_upstream: `84011`
- codes_db: `244077`
- codes_missing_in_db: `16`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260318_011107Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
