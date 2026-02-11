# Brickovery DB backup & change audit — 20260211_052359Z

## Context
- created_at_utc: **20260211_052359Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `174` (id `21893758569`)
- commit: `aaf603b6b4b45cdfbc186f4cf4ca384e775916aa`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `2f3546a5b7c2429036396ef6ee72f929b2b107488706ff661c49459dda8b7fc2`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260211_052359Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260211_052359Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `446aac8703f5ec4498fee3cee229cef396417177d782a9db2a66abaf5aff79f8`
- csv_size_bytes (pre-update): `25972422`
- csv_backup_file: `brickovery_db_csv_backup_20260211_052359Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202455`
- items_db: `202447`
- items_missing_in_db: `11`
- codes_upstream: `83311`
- codes_db: `242162`
- codes_missing_in_db: `6`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260211_052359Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
