# Brickovery DB backup & change audit — 20260831_020656Z

## Context
- created_at_utc: **20260831_020656Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3250` (id `33349295413`)
- commit: `21157c4a264d8cd0be356a0285b290828ac7e49e`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `f6b9b7fba9af523babf346934dc8ae80b27d496ddc78d8c411b720f827706286`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260831_020656Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260831_020656Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `433bed4ac042cbe727b78d55e271ea62d1eb5d7487387dffcb27badab95359b8`
- csv_size_bytes (pre-update): `26671254`
- csv_backup_file: `brickovery_db_csv_backup_20260831_020656Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209919`
- items_db: `210729`
- items_missing_in_db: `10`
- codes_upstream: `86352`
- codes_db: `254381`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260831_020656Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
