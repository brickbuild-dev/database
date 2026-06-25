# Brickovery DB backup & change audit — 20260625_021009Z

## Context
- created_at_utc: **20260625_021009Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3091` (id `28141980421`)
- commit: `ab126d0a3555cfc0429928db4141c2b7d34e9ad0`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `70e88340bfadbd7ec6a91dba607d1d808e9fd23d53f83700af0c2fde4e253f43`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260625_021009Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260625_021009Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `dfa2568fda7e1745fa7059d3fe8d22246949619d02597400db4631b080a9ca4a`
- csv_size_bytes (pre-update): `26430831`
- csv_backup_file: `brickovery_db_csv_backup_20260625_021009Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207450`
- items_db: `208005`
- items_missing_in_db: `104`
- codes_upstream: `84965`
- codes_db: `250177`
- codes_missing_in_db: `40`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260625_021009Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
