# Brickovery DB backup & change audit — 20260304_010359Z

## Context
- created_at_utc: **20260304_010359Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `371` (id `22650184760`)
- commit: `d9a32e4b30d12e45758027de07c72622e430e8fd`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `75b65e896befc54f9efd3ddca4b12da8b6bc701fc5ab8a283fdaa8f445e80e96`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260304_010359Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260304_010359Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `cfb8ba9738a43cddd05163b5039f3aee29ef502e00a52af75a9a19370cb82ddd`
- csv_size_bytes (pre-update): `26048216`
- csv_backup_file: `brickovery_db_csv_backup_20260304_010359Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203291`
- items_db: `203326`
- items_missing_in_db: `15`
- codes_upstream: `83779`
- codes_db: `243482`
- codes_missing_in_db: `20`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260304_010359Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
