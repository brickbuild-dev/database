# Brickovery DB backup & change audit — 20261015_021524Z

## Context
- created_at_utc: **20261015_021524Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3755` (id `38669351450`)
- commit: `434bef9cce1f7d8539f554f97f86793b541f96de`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `d62c559c14b9aa017af2dcb1fdae6bb5f35b7c0bcb919a601cdf6859fba65b05`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261015_021524Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261015_021524Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e5273ef914748a04aaa3a26d0dd46419b35403cc81627638e0e39a134e7e8337`
- csv_size_bytes (pre-update): `26885833`
- csv_backup_file: `brickovery_db_csv_backup_20261015_021524Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211611`
- items_db: `213458`
- items_missing_in_db: `7`
- codes_upstream: `86994`
- codes_db: `258105`
- codes_missing_in_db: `13`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261015_021524Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
