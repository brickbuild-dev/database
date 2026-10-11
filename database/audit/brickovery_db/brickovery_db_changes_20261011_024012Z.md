# Brickovery DB backup & change audit — 20261011_024012Z

## Context
- created_at_utc: **20261011_024012Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3666` (id `38105651045`)
- commit: `7b7d5ebf79fcb766910e3630c718c9392918916f`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `9d1eb80c29831e7efbea2ee5521a37116d8e857679d33cd98c1e0da89ae03622`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261011_024012Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261011_024012Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `f427cd142168f213ec6c0e2fd11253ce3421ab2036b2d7d7e6b047028ac0e07d`
- csv_size_bytes (pre-update): `26881505`
- csv_backup_file: `brickovery_db_csv_backup_20261011_024012Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211578`
- items_db: `213408`
- items_missing_in_db: `17`
- codes_upstream: `86955`
- codes_db: `258031`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261011_024012Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
