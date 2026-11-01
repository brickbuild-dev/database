# Brickovery DB backup & change audit — 20261101_031119Z

## Context
- created_at_utc: **20261101_031119Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3818` (id `41267092214`)
- commit: `9ff288804b692725bf974015a27ffd71407a83ad`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `9e58f4866f2f603e27665419851d60e0f75ac35fc76a868d38fff67d9e9ad02c`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261101_031119Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261101_031119Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `f9b10782e490d9498adb6c56ed7f6de21c4b7cb3a7efccb434660aa82605271d`
- csv_size_bytes (pre-update): `26917665`
- csv_backup_file: `brickovery_db_csv_backup_20261101_031119Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211996`
- items_db: `213869`
- items_missing_in_db: `5`
- codes_upstream: `87127`
- codes_db: `258662`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261101_031119Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
