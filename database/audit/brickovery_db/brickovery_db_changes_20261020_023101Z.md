# Brickovery DB backup & change audit — 20261020_023101Z

## Context
- created_at_utc: **20261020_023101Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3794` (id `39358718418`)
- commit: `55dcacf55d265310a99d144dfe6ab533431ed39d`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `8244d9827522fd68f7b7ad8b0b0e30a5812ed74f40c11286f4386dc33e98eea1`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261020_023101Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261020_023101Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `3e444954aa2cdfc910099ad571ce8187da830184ecaab939c76aea9670e939fd`
- csv_size_bytes (pre-update): `26892473`
- csv_backup_file: `brickovery_db_csv_backup_20261020_023101Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211687`
- items_db: `213538`
- items_missing_in_db: `16`
- codes_upstream: `87015`
- codes_db: `258220`
- codes_missing_in_db: `4`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261020_023101Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
