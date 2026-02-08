# Brickovery DB backup & change audit — 20260208_033323Z

## Context
- created_at_utc: **20260208_033323Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `158` (id `21791599808`)
- commit: `1d5356e578db57c27284847ac79068a5a4f5d925`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `32023d95569a0bdef03ead750e472abbe7863f34186f22daf7edbe0024bd36c8`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260208_033323Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260208_033323Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `7859de4b02af76d11943f8f8d5a054be9f916573b473c7d1e6118bd8f0b5ce52`
- csv_size_bytes (pre-update): `25970355`
- csv_backup_file: `brickovery_db_csv_backup_20260208_033323Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202428`
- items_db: `202422`
- items_missing_in_db: `8`
- codes_upstream: `83295`
- codes_db: `242127`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260208_033323Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
