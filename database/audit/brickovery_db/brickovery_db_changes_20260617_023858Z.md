# Brickovery DB backup & change audit — 20260617_023858Z

## Context
- created_at_utc: **20260617_023858Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3064` (id `27661876190`)
- commit: `e96a81640bdeebd0ef5fd09390aea41cbd2b4fa1`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `208db5089f9832e8f8e1be10f6d6fce4d91540a2ad1977f49587cfc7c8f80b2d`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260617_023858Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260617_023858Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d03aad625daabe1bf0c29bd04d9c325ec8ad7582729898638b55ef70fa0c8113`
- csv_size_bytes (pre-update): `26414560`
- csv_backup_file: `brickovery_db_csv_backup_20260617_023858Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207248`
- items_db: `207822`
- items_missing_in_db: `44`
- codes_upstream: `84874`
- codes_db: `249898`
- codes_missing_in_db: `21`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260617_023858Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
