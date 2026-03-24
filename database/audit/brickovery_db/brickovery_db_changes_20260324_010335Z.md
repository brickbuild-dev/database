# Brickovery DB backup & change audit — 20260324_010335Z

## Context
- created_at_utc: **20260324_010335Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `411` (id `23467967830`)
- commit: `a99ced381921c1d9204f8b2dd173f220d78b3437`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `4379ce502d6b978d1b74494021571e1eba083b5502846ec688795f69bc32243e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260324_010335Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260324_010335Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `a163353e4da6fccfde20f17a9815e3e5fd4a05ec839992eaae6879590d52b67c`
- csv_size_bytes (pre-update): `26094491`
- csv_backup_file: `brickovery_db_csv_backup_20260324_010335Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203778`
- items_db: `203867`
- items_missing_in_db: `4`
- codes_upstream: `84053`
- codes_db: `244293`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260324_010335Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
