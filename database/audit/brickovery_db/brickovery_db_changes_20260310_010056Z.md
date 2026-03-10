# Brickovery DB backup & change audit — 20260310_010056Z

## Context
- created_at_utc: **20260310_010056Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `383` (id `22882083795`)
- commit: `87742988780ba412cbae3c477f7626576aaee347`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `fc75860df9950f281b31f4d1c13d4cf9014ddf6e3d079026ad8b6751baba179b`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260310_010056Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260310_010056Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8697da5c436ddbc8e6ce2d19bd157329af63c946ee3f622994daf6056ee85c5f`
- csv_size_bytes (pre-update): `26065443`
- csv_backup_file: `brickovery_db_csv_backup_20260310_010056Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203435`
- items_db: `203483`
- items_missing_in_db: `10`
- codes_upstream: `83920`
- codes_db: `243781`
- codes_missing_in_db: `8`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260310_010056Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
