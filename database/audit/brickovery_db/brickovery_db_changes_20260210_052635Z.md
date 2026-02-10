# Brickovery DB backup & change audit — 20260210_052635Z

## Context
- created_at_utc: **20260210_052635Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `172` (id `21852885917`)
- commit: `fdad32648c4419894a0fcfa940da5f46852bc633`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `3af19026383314d208ea2f49c1be3af7a53b44a2133cfc5fc3c2b169b1bd4bab`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260210_052635Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260210_052635Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `54a08c4a48d4efb688a4a8298c069beff95993775074e615945a77310a80624f`
- csv_size_bytes (pre-update): `25971356`
- csv_backup_file: `brickovery_db_csv_backup_20260210_052635Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202445`
- items_db: `202439`
- items_missing_in_db: `8`
- codes_upstream: `83305`
- codes_db: `242144`
- codes_missing_in_db: `11`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260210_052635Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
