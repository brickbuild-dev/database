# Brickovery DB backup & change audit — 20260803_013524Z

## Context
- created_at_utc: **20260803_013524Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3194` (id `30776938135`)
- commit: `a9d788d1e2b5517a23ee2d2ec5e4b95938031b42`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `5159affedb9e59e808a5b3c8d1ccca1d1bf6c8565a88e4b688b96beae0f8dfbe`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260803_013524Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260803_013524Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8f073746c3efabeb83be99350dca6ebd8cf7d879a1dedd3ee01c409e9573fca7`
- csv_size_bytes (pre-update): `26588460`
- csv_backup_file: `brickovery_db_csv_backup_20260803_013524Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209073`
- items_db: `209802`
- items_missing_in_db: `34`
- codes_upstream: `85983`
- codes_db: `252946`
- codes_missing_in_db: `53`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260803_013524Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
