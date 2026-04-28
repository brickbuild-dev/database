# Brickovery DB backup & change audit — 20260428_015152Z

## Context
- created_at_utc: **20260428_015152Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2939` (id `25029394315`)
- commit: `85ba09fa6dbfb2f3362f33801ac7eb1a9f9e0f86`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `415d13ba3ff1ece05953d719a85b3768e7c5d547c13d0f57a1bd73714172eeb0`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260428_015152Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260428_015152Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `25be968780448fabc86bc8058b21590b8664bd7e605b4409af3d776fdea35ae3`
- csv_size_bytes (pre-update): `26210884`
- csv_backup_file: `brickovery_db_csv_backup_20260428_015152Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205354`
- items_db: `205726`
- items_missing_in_db: `2`
- codes_upstream: `84274`
- codes_db: `246361`
- codes_missing_in_db: `13`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260428_015152Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
