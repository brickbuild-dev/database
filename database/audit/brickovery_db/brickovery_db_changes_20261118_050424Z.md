# Brickovery DB backup & change audit — 20261118_050424Z

## Context
- created_at_utc: **20261118_050424Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3875` (id `44240686807`)
- commit: `7b13f160adb835e1ab0e0cfa6b2b1bdbfe4dee40`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `0c4375de739c255cc11de82da77e6a7693b884ac4e3bf021461c295de907c8cb`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261118_050424Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261118_050424Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `acfe4016573e21722ca13c600f627a7594cb9dd8988cba7a71c770aebd6785a8`
- csv_size_bytes (pre-update): `26930049`
- csv_backup_file: `brickovery_db_csv_backup_20261118_050424Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212154`
- items_db: `214026`
- items_missing_in_db: `10`
- codes_upstream: `87191`
- codes_db: `258876`
- codes_missing_in_db: `8`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261118_050424Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
