# Brickovery DB backup & change audit — 20260301_011237Z

## Context
- created_at_utc: **20260301_011237Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `365` (id `22532970046`)
- commit: `b7de2d01cb024337b81d5a2317d5a70467572f36`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `346eee88d78b0cdacd76e8f500b5a156bac88569aa4a31e4f6f7f0ca83f7acc7`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260301_011237Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260301_011237Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `acbd39b54dbbe89def47a23a7afe389e97483e821cb53301eafb6b673c8307ba`
- csv_size_bytes (pre-update): `25994008`
- csv_backup_file: `brickovery_db_csv_backup_20260301_011237Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202999`
- items_db: `202599`
- items_missing_in_db: `446`
- codes_upstream: `83654`
- codes_db: `242539`
- codes_missing_in_db: `120`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260301_011237Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
