# Brickovery DB backup & change audit — 20260909_020014Z

## Context
- created_at_utc: **20260909_020014Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3356` (id `34300980800`)
- commit: `dd0ea956bec35cfb06a103ee6b665ab9d86e28ee`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `e9ba698a5570f329b5b678fb7f437c88a517bd8c3fed2be2151c2c893402265a`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260909_020014Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260909_020014Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `3a8955f386c27d3890eb5b172e0f0316aac665b439268bf9bffd19800d945ada`
- csv_size_bytes (pre-update): `26714235`
- csv_backup_file: `brickovery_db_csv_backup_20260909_020014Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210521`
- items_db: `211298`
- items_missing_in_db: `63`
- codes_upstream: `86572`
- codes_db: `255115`
- codes_missing_in_db: `44`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260909_020014Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
