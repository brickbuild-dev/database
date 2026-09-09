# Brickovery DB backup & change audit — 20260909_025936Z

## Context
- created_at_utc: **20260909_025936Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3362` (id `34304932322`)
- commit: `07ac68eabafd7c47d388d9193c295b7507ff5ca7`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `216adf325ffcf3ed5c84954ccaa9f25e7c7a158a001411f2455390cc3fd428ac`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260909_025936Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260909_025936Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d0f5ce3c4c3160c53282b1f2b6685a32dcdcbd59fa531b8542cc30a88339e210`
- csv_size_bytes (pre-update): `26720321`
- csv_backup_file: `brickovery_db_csv_backup_20260909_025936Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210521`
- items_db: `211361`
- items_missing_in_db: `0`
- codes_upstream: `86578`
- codes_db: `255221`
- codes_missing_in_db: `6`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260909_025936Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
