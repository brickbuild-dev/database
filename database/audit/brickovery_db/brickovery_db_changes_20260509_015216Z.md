# Brickovery DB backup & change audit — 20260509_015216Z

## Context
- created_at_utc: **20260509_015216Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2961` (id `25588206005`)
- commit: `cadb26873fe19e6872494ee48ddb00ff3b1bbe1c`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `d1bcbbedc2590e5d0c9981a53717995253d2d8061e5425404b28b0acf84fd026`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260509_015216Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260509_015216Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `f693424b38988201fc989146b57e64399a9d391b3a07abd50b322da6ab9c8556`
- csv_size_bytes (pre-update): `26279329`
- csv_backup_file: `brickovery_db_csv_backup_20260509_015216Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205723`
- items_db: `206137`
- items_missing_in_db: `27`
- codes_upstream: `84204`
- codes_db: `247543`
- codes_missing_in_db: `22`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260509_015216Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
