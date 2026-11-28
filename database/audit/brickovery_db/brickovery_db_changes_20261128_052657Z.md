# Brickovery DB backup & change audit — 20261128_052657Z

## Context
- created_at_utc: **20261128_052657Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3910` (id `46111436146`)
- commit: `4d5205b7ca17a83fc241c9ff20996a4711c030d9`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `65db880d4115543297dd795a3f4db85cc705c65eca041b9eee18d0d8c30ba286`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261128_052657Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261128_052657Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `5d204370b9853c408908e3aa201ea8b10a6d15f52c11be3ab948f127cdd36a88`
- csv_size_bytes (pre-update): `26935547`
- csv_backup_file: `brickovery_db_csv_backup_20261128_052657Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212229`
- items_db: `214103`
- items_missing_in_db: `12`
- codes_upstream: `87207`
- codes_db: `258970`
- codes_missing_in_db: `6`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261128_052657Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
