# Brickovery DB backup & change audit — 20260807_020726Z

## Context
- created_at_utc: **20260807_020726Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3202` (id `31139813366`)
- commit: `e836970d63f8b567c35a25cf2924fae310bd64b3`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `d26915eededa6ce59fef4e9823b221ccf0e4e79cb69a4617d6712860cc6a3e7f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260807_020726Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260807_020726Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `69f71f141726de6b89b44d1fe40dee5f351f23c4fda43c8240a799be76169730`
- csv_size_bytes (pre-update): `26605330`
- csv_backup_file: `brickovery_db_csv_backup_20260807_020726Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209261`
- items_db: `210007`
- items_missing_in_db: `28`
- codes_upstream: `86028`
- codes_db: `253248`
- codes_missing_in_db: `13`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260807_020726Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
