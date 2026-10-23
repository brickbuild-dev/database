# Brickovery DB backup & change audit — 20261023_022725Z

## Context
- created_at_utc: **20261023_022725Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3800` (id `39888813218`)
- commit: `25aad17eba2c215de5e5122db6931c5b6591a4c9`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `2d039648e6317802e962dd4488cac59c550848991aa5130bcba20f46fb6dc0fc`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261023_022725Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261023_022725Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `342ffc14e5b182a42cd45172b5b37e1af494b936d21f20aed374bb33663ddd9e`
- csv_size_bytes (pre-update): `26898203`
- csv_backup_file: `brickovery_db_csv_backup_20261023_022725Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211762`
- items_db: `213618`
- items_missing_in_db: `11`
- codes_upstream: `87032`
- codes_db: `258321`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261023_022725Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
