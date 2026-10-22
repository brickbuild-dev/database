# Brickovery DB backup & change audit — 20261022_022127Z

## Context
- created_at_utc: **20261022_022127Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3798` (id `39710060704`)
- commit: `3926f0b0ccf7e65c466d1c6305f4df376a52e411`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `261e2a3e5531b4f5f7138463619c7bc39a8778fdf8cd9b8d9e23063f74e9aac8`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261022_022127Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261022_022127Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d0a059390ed093a84603aadababaf4c9c9824b190c41adcb84ccc86c48f05077`
- csv_size_bytes (pre-update): `26894840`
- csv_backup_file: `brickovery_db_csv_backup_20261022_022127Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211751`
- items_db: `213573`
- items_missing_in_db: `45`
- codes_upstream: `87032`
- codes_db: `258262`
- codes_missing_in_db: `14`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261022_022127Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
