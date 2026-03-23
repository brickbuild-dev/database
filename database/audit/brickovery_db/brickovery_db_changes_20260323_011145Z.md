# Brickovery DB backup & change audit — 20260323_011145Z

## Context
- created_at_utc: **20260323_011145Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `409` (id `23417150406`)
- commit: `00390c657df7c8fb6f70dea38f5b0f82f4907e2e`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `91119db3dfec7850faf0fb1c1cfc579b6fcb56617c23d8ce92c8d0f1526b834d`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260323_011145Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260323_011145Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `2c0ed6e7b02bfd27963ad3ebfdc878f6432c468103428acf45301af40caf5c77`
- csv_size_bytes (pre-update): `26091360`
- csv_backup_file: `brickovery_db_csv_backup_20260323_011145Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203775`
- items_db: `203809`
- items_missing_in_db: `58`
- codes_upstream: `84052`
- codes_db: `244233`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260323_011145Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
