# Brickovery DB backup & change audit — 20261016_020547Z

## Context
- created_at_utc: **20261016_020547Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3757` (id `38837956463`)
- commit: `4cf31405f5c7791340fe6d33ac71d0b086f438f8`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `f72d3dd76b62a55a1160af0050e9dc893c7206f88599befbb5524ded500712ca`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261016_020547Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261016_020547Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `4dd77646f2592efb058497590ac5da70666841951a90c572d485663d34674aa2`
- csv_size_bytes (pre-update): `26886971`
- csv_backup_file: `brickovery_db_csv_backup_20261016_020547Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211618`
- items_db: `213465`
- items_missing_in_db: `9`
- codes_upstream: `86995`
- codes_db: `258125`
- codes_missing_in_db: `8`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261016_020547Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
