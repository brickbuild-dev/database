# Brickovery DB backup & change audit — 20261006_034216Z

## Context
- created_at_utc: **20261006_034216Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3656` (id `37409766827`)
- commit: `2e6bcc7486a9723ec266dad048059e5e1ea60693`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `ac540158bf4621490eb1c01f358be01ca4032f3faa6f586474c9d16689fe9ee6`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261006_034216Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261006_034216Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `4cfdd1a3c3a600f4d6d3a09ab66bbf74912ef11297edf57ba0f0f9cde8f8324f`
- csv_size_bytes (pre-update): `26867207`
- csv_backup_file: `brickovery_db_csv_backup_20261006_034216Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211488`
- items_db: `213294`
- items_missing_in_db: `35`
- codes_upstream: `86859`
- codes_db: `257786`
- codes_missing_in_db: `36`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261006_034216Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
