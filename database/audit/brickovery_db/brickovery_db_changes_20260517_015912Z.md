# Brickovery DB backup & change audit — 20260517_015912Z

## Context
- created_at_utc: **20260517_015912Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2973` (id `25978459149`)
- commit: `ace26d03c3a6ed7b1949533b3550f73993dfa6bb`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `adec1489ad39e7eeb00fd0a4145f7571800cbe7bb84076a2f59b9f7b5b7881aa`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260517_015912Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260517_015912Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8e617ec72c3086354cd8f980b486d31b4019ed01ae814f3ed82f95a7efa7c56b`
- csv_size_bytes (pre-update): `26300015`
- csv_backup_file: `brickovery_db_csv_backup_20260517_015912Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205860`
- items_db: `206321`
- items_missing_in_db: `13`
- codes_upstream: `84369`
- codes_db: `247898`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260517_015912Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
