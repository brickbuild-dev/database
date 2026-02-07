# Brickovery DB backup & change audit — 20260207_180126Z

## Context
- created_at_utc: **20260207_180126Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `152` (id `21784444710`)
- commit: `774fda4b73e1118e29a61b6c481c12140bdb3fa4`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `8f2f7ba861800eb11f3d1ab35233a035ee54018988fc6a189ba75abf96842df4`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260207_180126Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260207_180126Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `3e2742a60cc6fc5ed30ea6a68772ecee4e20fa2a32c9fb449eb3c04625f8f759`
- csv_size_bytes (pre-update): `25969769`
- csv_backup_file: `brickovery_db_csv_backup_20260207_180126Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202420`
- items_db: `202417`
- items_missing_in_db: `5`
- codes_upstream: `83295`
- codes_db: `242117`
- codes_missing_in_db: `5`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260207_180126Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
