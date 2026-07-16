# Brickovery DB backup & change audit — 20260716_012939Z

## Context
- created_at_utc: **20260716_012939Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3159` (id `29463932471`)
- commit: `01e24e580ad0b144f06461489a78111c9766a0ee`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `9a603be2c15804e29f1b210ae3f93c2fbcf1afeee3da0ff11014b59539012f27`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260716_012939Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260716_012939Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `75bd27df8f022b060f696697c68f6aa0a110dde2299b0df7729c93c55e71b1e9`
- csv_size_bytes (pre-update): `26487364`
- csv_backup_file: `brickovery_db_csv_backup_20260716_012939Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207865`
- items_db: `208551`
- items_missing_in_db: `6`
- codes_upstream: `85366`
- codes_db: `251151`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260716_012939Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
