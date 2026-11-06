# Brickovery DB backup & change audit — 20261106_040548Z

## Context
- created_at_utc: **20261106_040548Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3857` (id `42159527370`)
- commit: `191f613a881542e28e6df24fb287134191a9d184`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `0d3fe3d1c9f8117a7102073212b2508afbf63f7f34439953c6ffc8a5b794cb15`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261106_040548Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261106_040548Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `c83d98eac6af05b677d2e6110d9e43af2d69bc70ce80717a7bf409e545519c11`
- csv_size_bytes (pre-update): `26923513`
- csv_backup_file: `brickovery_db_csv_backup_20261106_040548Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212087`
- items_db: `213944`
- items_missing_in_db: `23`
- codes_upstream: `87174`
- codes_db: `258763`
- codes_missing_in_db: `25`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261106_040548Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
