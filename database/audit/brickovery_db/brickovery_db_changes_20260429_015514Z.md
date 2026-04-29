# Brickovery DB backup & change audit — 20260429_015514Z

## Context
- created_at_utc: **20260429_015514Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2941` (id `25086934420`)
- commit: `42c94149b52da03fd3d550dc8f3c22b7f11f734a`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `0166c7824217386eebb8a20db3558458cf640a2f4033a60ee72afe16ffe8f028`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260429_015514Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260429_015514Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `41d9ffa8cb762c60d782e2d9edd3c46064669227bb79b12be8fc3c5498d3df90`
- csv_size_bytes (pre-update): `26211798`
- csv_backup_file: `brickovery_db_csv_backup_20260429_015514Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205373`
- items_db: `205728`
- items_missing_in_db: `19`
- codes_upstream: `84327`
- codes_db: `246376`
- codes_missing_in_db: `53`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260429_015514Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
