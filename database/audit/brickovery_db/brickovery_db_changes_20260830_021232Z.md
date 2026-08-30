# Brickovery DB backup & change audit — 20260830_021232Z

## Context
- created_at_utc: **20260830_021232Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3248` (id `33287125944`)
- commit: `1fd470bca7bc4f420c63cb73b6a30bd170770899`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `838d36f026adf34e2d7a1e55ebcad41e0c9081e771ce9b125e7acb83e88f761c`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260830_021232Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260830_021232Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `0fde7e9ed443ec705262a4c08fde472901fa167d147c2c2e1d9a5ccfe8eb3b0b`
- csv_size_bytes (pre-update): `26670052`
- csv_backup_file: `brickovery_db_csv_backup_20260830_021232Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209910`
- items_db: `210711`
- items_missing_in_db: `18`
- codes_upstream: `86351`
- codes_db: `254360`
- codes_missing_in_db: `6`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260830_021232Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
