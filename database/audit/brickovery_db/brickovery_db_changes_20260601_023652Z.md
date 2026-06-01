# Brickovery DB backup & change audit — 20260601_023652Z

## Context
- created_at_utc: **20260601_023652Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3003` (id `26732046550`)
- commit: `439dcb73c43f2d33a8ba81d05b942d7c3760ffdb`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `27f7d1e33e6472e99b338c1f7b3613c69ad8f88a83ff088649f030897291c3f5`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260601_023652Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260601_023652Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8f036d3881630dcfa314a71b38d690fc33eec42f2ac33df9c28113de64681ba5`
- csv_size_bytes (pre-update): `26322942`
- csv_backup_file: `brickovery_db_csv_backup_20260601_023652Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206097`
- items_db: `206632`
- items_missing_in_db: `50`
- codes_upstream: `84410`
- codes_db: `248306`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260601_023652Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
