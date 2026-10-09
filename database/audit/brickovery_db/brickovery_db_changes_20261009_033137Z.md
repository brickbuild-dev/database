# Brickovery DB backup & change audit — 20261009_033137Z

## Context
- created_at_utc: **20261009_033137Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3662` (id `37879127130`)
- commit: `7fa6db5d3dd1e1e3fc85a6c7f50045b873b32f03`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `66651b7a88608b51ccc47e7aecff3ebbab0aeb1946ee39cf2003411cfad10bd4`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261009_033137Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261009_033137Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `42ee7a86361463898bfe412d982bfff06dec0b9942a2d582f3354545f9fe2918`
- csv_size_bytes (pre-update): `26876459`
- csv_backup_file: `brickovery_db_csv_backup_20261009_033137Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211551`
- items_db: `213372`
- items_missing_in_db: `26`
- codes_upstream: `86940`
- codes_db: `257945`
- codes_missing_in_db: `37`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261009_033137Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
