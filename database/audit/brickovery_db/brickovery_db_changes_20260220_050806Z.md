# Brickovery DB backup & change audit — 20260220_050806Z

## Context
- created_at_utc: **20260220_050806Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `354` (id `22212131338`)
- commit: `6582f828abe513a33e60155a92d4ced1fad73c2d`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `0a1b7471a82755f236447a85d6db06e533e5323804a3d1424d75d043272b0dfd`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260220_050806Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260220_050806Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `6014320e47c990c86aef226af60db61d4b23843fd2b4f97a5eb60a4f62aa020d`
- csv_size_bytes (pre-update): `25986487`
- csv_backup_file: `brickovery_db_csv_backup_20260220_050806Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202587`
- items_db: `202557`
- items_missing_in_db: `37`
- codes_upstream: `83445`
- codes_db: `242407`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260220_050806Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
