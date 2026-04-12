# Brickovery DB backup & change audit — 20260412_012522Z

## Context
- created_at_utc: **20260412_012522Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2886` (id `24295759464`)
- commit: `bde0cb368647e599136cd8a53ccdc5ceb1b201c4`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `7c080f2f76844952900b61d978c9a776bb1fa6c866a5f7f8bf6e057852220dcb`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260412_012522Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260412_012522Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `532580589d2447f60a9c755e42e92d3829569fad57f14f6fd734f75187c16dec`
- csv_size_bytes (pre-update): `26190973`
- csv_backup_file: `brickovery_db_csv_backup_20260412_012522Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205178`
- items_db: `205510`
- items_missing_in_db: `14`
- codes_upstream: `84144`
- codes_db: `246014`
- codes_missing_in_db: `6`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260412_012522Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
