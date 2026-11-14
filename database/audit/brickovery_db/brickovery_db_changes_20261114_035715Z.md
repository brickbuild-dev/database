# Brickovery DB backup & change audit — 20261114_035715Z

## Context
- created_at_utc: **20261114_035715Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3867` (id `43553721137`)
- commit: `24aec31e8ee49f4784729454c5caea859ec2481f`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `4d1c01c12410291d76410348aa66a76659e3c358ffe684ad268f5c23feae9f2e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261114_035715Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261114_035715Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `c2644a8dd1b674f24c0bbb5ec85c0caf6ba9596cc96badc63d6dead89c67b347`
- csv_size_bytes (pre-update): `26926251`
- csv_backup_file: `brickovery_db_csv_backup_20261114_035715Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212090`
- items_db: `213969`
- items_missing_in_db: `1`
- codes_upstream: `87181`
- codes_db: `258811`
- codes_missing_in_db: `6`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261114_035715Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
