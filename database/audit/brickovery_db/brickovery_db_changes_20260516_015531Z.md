# Brickovery DB backup & change audit — 20260516_015531Z

## Context
- created_at_utc: **20260516_015531Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2971` (id `25949676713`)
- commit: `ada6576d4c8df84b489411f75a276469a17e840b`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `44d6745c238f816c09f1b597646e25af525fb9b3c63b51c7a4c5b59f3b36e64c`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260516_015531Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260516_015531Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `f90e3cdcaf069253d13ebd20691eafecacaf49833aba346b8392111f7e5a6a97`
- csv_size_bytes (pre-update): `26299536`
- csv_backup_file: `brickovery_db_csv_backup_20260516_015531Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205849`
- items_db: `206315`
- items_missing_in_db: `6`
- codes_upstream: `84369`
- codes_db: `247890`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260516_015531Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
