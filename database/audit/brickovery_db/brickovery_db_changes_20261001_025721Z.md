# Brickovery DB backup & change audit — 20261001_025721Z

## Context
- created_at_utc: **20261001_025721Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3546` (id `36807644125`)
- commit: `d21b2b2b92a33ec8510565f386a88b19fc3bc447`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `c7febffaecadac08584a7c30adbb99e57ba20844897def3ba4b82fdc8d987b52`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261001_025721Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261001_025721Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `bca8376bfbe2e2a582caa8b8aa74f451279ea2f9c605023deda19788950973ca`
- csv_size_bytes (pre-update): `26851022`
- csv_backup_file: `brickovery_db_csv_backup_20261001_025721Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211286`
- items_db: `213107`
- items_missing_in_db: `15`
- codes_upstream: `86737`
- codes_db: `257509`
- codes_missing_in_db: `12`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261001_025721Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
