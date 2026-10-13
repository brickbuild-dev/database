# Brickovery DB backup & change audit — 20261013_042509Z

## Context
- created_at_utc: **20261013_042509Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3751` (id `38345519812`)
- commit: `dc795641180e2ba3c8cb1fefd1268e4f025906f9`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `8f7b5a5378581639ef709f0854c79037653c1d597571d6a4cedda2c474918917`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261013_042509Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261013_042509Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `525e04bc5dcdbdc833cf724f3c1486d801ccffa7811b2cee42a1ea296069e7a7`
- csv_size_bytes (pre-update): `26885269`
- csv_backup_file: `brickovery_db_csv_backup_20261013_042509Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211600`
- items_db: `213449`
- items_missing_in_db: `5`
- codes_upstream: `86980`
- codes_db: `258095`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261013_042509Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
