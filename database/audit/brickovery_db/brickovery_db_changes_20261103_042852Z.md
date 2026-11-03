# Brickovery DB backup & change audit — 20261103_042852Z

## Context
- created_at_utc: **20261103_042852Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3822` (id `41577571101`)
- commit: `feb5020a551c9be498d9f89454f545af6d7e4b0f`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `801a277eecdc06942bc6a674ba0860097151b48b6551eb2e36aec9d039043d5c`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261103_042852Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261103_042852Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `3fec0a969e4dfb559aeac5ec4e3db30358675dcd75911030b98d2302115e5d17`
- csv_size_bytes (pre-update): `26919955`
- csv_backup_file: `brickovery_db_csv_backup_20261103_042852Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212060`
- items_db: `213902`
- items_missing_in_db: `37`
- codes_upstream: `87146`
- codes_db: `258702`
- codes_missing_in_db: `15`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261103_042852Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
