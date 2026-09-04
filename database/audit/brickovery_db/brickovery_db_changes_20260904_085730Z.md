# Brickovery DB backup & change audit — 20260904_085730Z

## Context
- created_at_utc: **20260904_085730Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3331` (id `33855376432`)
- commit: `87da7c388c0d2bd85bdf587585db56a99a9c098b`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `19cb032261f16ba3e125e6770f5505d70aeb0cf9bbd72faf19daf88aff1504b2`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260904_085730Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260904_085730Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d012d3bf47ef097ed9299fe01fc17642e5b9d3a90721172e0551555615b18c54`
- csv_size_bytes (pre-update): `26693384`
- csv_backup_file: `brickovery_db_csv_backup_20260904_085730Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210232`
- items_db: `211062`
- items_missing_in_db: `6`
- codes_upstream: `86403`
- codes_db: `254757`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260904_085730Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
