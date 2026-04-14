# Brickovery DB backup & change audit — 20260414_012610Z

## Context
- created_at_utc: **20260414_012610Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2890` (id `24375739173`)
- commit: `f6760e3665003ca02bedcfa42329f5c831adc01c`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `9d74ad79c0c35f96df9d7bc217fa53982b1ca899e738d6595321cfb85a3d8f07`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260414_012610Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260414_012610Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `663d51235213dfd2d30cd76286e761ded630aa26c4d5d36ed466301a65902127`
- csv_size_bytes (pre-update): `26192379`
- csv_backup_file: `brickovery_db_csv_backup_20260414_012610Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205189`
- items_db: `205531`
- items_missing_in_db: `6`
- codes_upstream: `84149`
- codes_db: `246039`
- codes_missing_in_db: `5`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260414_012610Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
