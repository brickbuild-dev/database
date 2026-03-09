# Brickovery DB backup & change audit — 20260309_010703Z

## Context
- created_at_utc: **20260309_010703Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `381` (id `22834179090`)
- commit: `649cff825417070d3db9c481b2305888cfc2f8a4`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `52e38272125547fda8e251903410a9bbfb730467d55853b577c452a00899b9df`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260309_010703Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260309_010703Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `3fdba45e554353cb8ae0d8e33602554c0b74f6367a71b97bacbcd9388654a620`
- csv_size_bytes (pre-update): `26060391`
- csv_backup_file: `brickovery_db_csv_backup_20260309_010703Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203425`
- items_db: `203445`
- items_missing_in_db: `38`
- codes_upstream: `83912`
- codes_db: `243694`
- codes_missing_in_db: `50`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260309_010703Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
