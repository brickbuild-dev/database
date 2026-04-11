# Brickovery DB backup & change audit — 20260411_011654Z

## Context
- created_at_utc: **20260411_011654Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2836` (id `24271199159`)
- commit: `20175c3ef798892d9ef0c219857da7bf02ef1917`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `5847780c34370531903f2452a94d8ea0a94eac7aa6721ff26dce0222cf9d76eb`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260411_011654Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260411_011654Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `0d36f6f726ecbcb37dc1cd75a7a561c3e6506755ae952e05a98e0db9663130c1`
- csv_size_bytes (pre-update): `26188774`
- csv_backup_file: `brickovery_db_csv_backup_20260411_011654Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205173`
- items_db: `205484`
- items_missing_in_db: `24`
- codes_upstream: `84139`
- codes_db: `245976`
- codes_missing_in_db: `7`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260411_011654Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
