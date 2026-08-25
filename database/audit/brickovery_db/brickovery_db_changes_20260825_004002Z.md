# Brickovery DB backup & change audit — 20260825_004002Z

## Context
- created_at_utc: **20260825_004002Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3238` (id `32794079406`)
- commit: `9fba16b5102daf0a6d9f956c5e16513ee99cbb51`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `458bceb8943c0e37f2001a4a020a7422df370706126bccba38d054593dc1242e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260825_004002Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260825_004002Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `0f64114bb0a70a6693dc8cfc62e87a2d98df6d8af9165de4c1abf26b04a30f40`
- csv_size_bytes (pre-update): `26657916`
- csv_backup_file: `brickovery_db_csv_backup_20260825_004002Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209827`
- items_db: `210587`
- items_missing_in_db: `38`
- codes_upstream: `86329`
- codes_db: `254154`
- codes_missing_in_db: `18`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260825_004002Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
