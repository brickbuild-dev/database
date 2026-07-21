# Brickovery DB backup & change audit — 20260721_013028Z

## Context
- created_at_utc: **20260721_013028Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3168` (id `29792963107`)
- commit: `a687be9d82284e38de61abc79da6af9e9982a4bb`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `e3c3810a5947a749c31b886bdee024881130eeaeaa35dce51ef7ecaf6fa76f3a`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260721_013028Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260721_013028Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `ed0f9f37515369a85e122ffab0bf948d4993c1e84798c0de7bd2322fbc86fb6c`
- csv_size_bytes (pre-update): `26489933`
- csv_backup_file: `brickovery_db_csv_backup_20260721_013028Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `208019`
- items_db: `208588`
- items_missing_in_db: `131`
- codes_upstream: `85403`
- codes_db: `251195`
- codes_missing_in_db: `31`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260721_013028Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
