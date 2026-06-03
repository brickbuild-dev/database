# Brickovery DB backup & change audit — 20260603_024143Z

## Context
- created_at_utc: **20260603_024143Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3007` (id `26860262049`)
- commit: `d5804bd91820f179e606611248f0714512ce7f13`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `30cc0d83dd5e8fb4d91779247d2ff08d98f14d502ad391149fcfe5b51768dced`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260603_024143Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260603_024143Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `f1eaf139543d5406758d602ffc6ce7621a4b37cfd69392374ea5fc2584cc1ee4`
- csv_size_bytes (pre-update): `26348840`
- csv_backup_file: `brickovery_db_csv_backup_20260603_024143Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206502`
- items_db: `207049`
- items_missing_in_db: `44`
- codes_upstream: `84437`
- codes_db: `248739`
- codes_missing_in_db: `11`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260603_024143Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
