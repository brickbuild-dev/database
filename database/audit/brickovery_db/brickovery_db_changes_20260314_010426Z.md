# Brickovery DB backup & change audit — 20260314_010426Z

## Context
- created_at_utc: **20260314_010426Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `391` (id `23076771927`)
- commit: `8083256d923d2d9c7d5f82eb4ff93f2fb51db864`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `00e2a38d09e53c283b7015386a1e710386211f0188900c7ebb721cec628d8549`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260314_010426Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260314_010426Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `30c046a1d95cb9bb7ff8293211d7582f7080215603ced198718cf4112802ba97`
- csv_size_bytes (pre-update): `26070825`
- csv_backup_file: `brickovery_db_csv_backup_20260314_010426Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203517`
- items_db: `203553`
- items_missing_in_db: `34`
- codes_upstream: `83951`
- codes_db: `243875`
- codes_missing_in_db: `9`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260314_010426Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
