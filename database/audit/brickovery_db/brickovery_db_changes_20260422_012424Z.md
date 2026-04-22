# Brickovery DB backup & change audit — 20260422_012424Z

## Context
- created_at_utc: **20260422_012424Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2926` (id `24755108756`)
- commit: `247ce4ff9d86463acffdbd67d855e8c8adcb0ff4`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `a132197db368fcd6d8110b65f01506b98822f4174a153a84776d3ad46d0bfdc9`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260422_012424Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260422_012424Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `c8977e05733d56b242a42a472df56eaf43e1da83bf0b8333563b5cfe0e250897`
- csv_size_bytes (pre-update): `26199806`
- csv_backup_file: `brickovery_db_csv_backup_20260422_012424Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205278`
- items_db: `205620`
- items_missing_in_db: `24`
- codes_upstream: `84171`
- codes_db: `246168`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260422_012424Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
