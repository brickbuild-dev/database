# Brickovery DB backup & change audit — 20260929_030831Z

## Context
- created_at_utc: **20260929_030831Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3542` (id `36515352694`)
- commit: `7a8afe35191fcde6945a8dfae54c0e6219d6818b`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `1be5e7b4a59e15b42ca8e6c8f5340b93c271a260c90969883b8d008a86d40e55`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260929_030831Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260929_030831Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d554efdd04b81ca3311565cfdb8f86b40aacd66b5c9d585bbaa5cb7cb956d15a`
- csv_size_bytes (pre-update): `26772688`
- csv_backup_file: `brickovery_db_csv_backup_20260929_030831Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211232`
- items_db: `212151`
- items_missing_in_db: `18`
- codes_upstream: `86721`
- codes_db: `256170`
- codes_missing_in_db: `10`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260929_030831Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
