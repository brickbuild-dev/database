# Brickovery DB backup & change audit — 20260212_051851Z

## Context
- created_at_utc: **20260212_051851Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `176` (id `21934558292`)
- commit: `6aa7a8a402793a52cfedd761bc1f1c1978106cae`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `71d5c3716330e97e7e4cc2a2e08e012340024b77a7c0e19abcbc8a32c66d7bd1`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260212_051851Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260212_051851Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `c1fd62ac444df8c3b74680cc211619aac0f2672be77cd82c5e8fb594c2db4f58`
- csv_size_bytes (pre-update): `25973411`
- csv_backup_file: `brickovery_db_csv_backup_20260212_051851Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202460`
- items_db: `202458`
- items_missing_in_db: `5`
- codes_upstream: `83312`
- codes_db: `242179`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260212_051851Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
