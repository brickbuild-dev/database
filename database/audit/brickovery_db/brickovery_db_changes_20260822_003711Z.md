# Brickovery DB backup & change audit — 20260822_003711Z

## Context
- created_at_utc: **20260822_003711Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3232` (id `32540643408`)
- commit: `af758d1121deedffdff3895c56c88d39a7648674`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `58a2ea8781bb2895a963cfc9b1ce7ef368a2d947b8624c5af82c4f6f8d546fe5`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260822_003711Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260822_003711Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `1eb551fcdc89c17994d9ce3e7be43944a86c8b8c069984bc288691f837d25fe1`
- csv_size_bytes (pre-update): `26653699`
- csv_backup_file: `brickovery_db_csv_backup_20260822_003711Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209778`
- items_db: `210563`
- items_missing_in_db: `13`
- codes_upstream: `86299`
- codes_db: `254084`
- codes_missing_in_db: `34`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260822_003711Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
