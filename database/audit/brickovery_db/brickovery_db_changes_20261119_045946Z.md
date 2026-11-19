# Brickovery DB backup & change audit — 20261119_045946Z

## Context
- created_at_utc: **20261119_045946Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3877` (id `44460921591`)
- commit: `1e8ba7ca61964a1f6692818e9031b19119ec25f9`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `6b58f2af313d19a669a1316e8909fa36480abb5bb5046b460443d658991e9365`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261119_045946Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261119_045946Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `04c82f70d9956b7ffeecc9cc1889c757515efa67e9735ebb11bbbd2c2efd9ade`
- csv_size_bytes (pre-update): `26931108`
- csv_backup_file: `brickovery_db_csv_backup_20261119_045946Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212168`
- items_db: `214036`
- items_missing_in_db: `14`
- codes_upstream: `87191`
- codes_db: `258894`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261119_045946Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
