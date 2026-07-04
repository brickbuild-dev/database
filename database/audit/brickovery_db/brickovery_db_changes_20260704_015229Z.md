# Brickovery DB backup & change audit — 20260704_015229Z

## Context
- created_at_utc: **20260704_015229Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3108` (id `28691177560`)
- commit: `7562cf79ea6470445a9d9c555340e5723975d1c1`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `e3073b203a73b579ed070c6b2e4767cfcc9dc2f7e5b29921af9847594e88b6da`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260704_015229Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260704_015229Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d790af51da4bdec6a7284d944637e5bbc668038e3bafabb38dcdba5f8c4613a1`
- csv_size_bytes (pre-update): `26462960`
- csv_backup_file: `brickovery_db_csv_backup_20260704_015229Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207702`
- items_db: `208325`
- items_missing_in_db: `55`
- codes_upstream: `85194`
- codes_db: `250729`
- codes_missing_in_db: `30`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260704_015229Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
