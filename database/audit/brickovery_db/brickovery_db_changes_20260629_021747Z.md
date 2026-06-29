# Brickovery DB backup & change audit — 20260629_021747Z

## Context
- created_at_utc: **20260629_021747Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3099` (id `28344278421`)
- commit: `c24b6f3a8a020a1d348030616e3b1d68ecdc2c55`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `cbac16c20209e1b5c6b5da0ecf35336e94cf054ac2888f1b7f8ecee6c2f26781`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260629_021747Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260629_021747Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `cccc78fc17f3be4bcdf7f6d6d7225bd865cee42b0c93c7713a27a951c67947e9`
- csv_size_bytes (pre-update): `26450242`
- csv_backup_file: `brickovery_db_csv_backup_20260629_021747Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207547`
- items_db: `208207`
- items_missing_in_db: `14`
- codes_upstream: `85071`
- codes_db: `250509`
- codes_missing_in_db: `10`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260629_021747Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
