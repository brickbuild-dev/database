# Brickovery DB backup & change audit — 20260221_045341Z

## Context
- created_at_utc: **20260221_045341Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `356` (id `22250654337`)
- commit: `81e18841db2a85a6c2effb86a26abb4532ad79df`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `cb9d836afd5571786397cc4398b2df11f84661e662685058710afed9dafc3477`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260221_045341Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260221_045341Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `b72fe57077490b07413276eb00a1dd6dac2b2a23c58cfef736a5ed5e431bfbad`
- csv_size_bytes (pre-update): `25988624`
- csv_backup_file: `brickovery_db_csv_backup_20260221_045341Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202591`
- items_db: `202594`
- items_missing_in_db: `5`
- codes_upstream: `83533`
- codes_db: `242445`
- codes_missing_in_db: `89`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260221_045341Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
