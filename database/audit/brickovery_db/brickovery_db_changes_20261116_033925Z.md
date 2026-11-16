# Brickovery DB backup & change audit — 20261116_033925Z

## Context
- created_at_utc: **20261116_033925Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3871` (id `43798730467`)
- commit: `4fa3c298f027ff17254a07047f16cf6d298066a3`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `2ea63a3123aeb4bd4af2d5471f56c51917157b18a2f4d1f99881c7c39044cd91`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261116_033925Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261116_033925Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `2eb7e2d186b9f6c3588ab1b378fc6bb52d91f92ca557be75628d25509e98b6f3`
- csv_size_bytes (pre-update): `26928147`
- csv_backup_file: `brickovery_db_csv_backup_20261116_033925Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212125`
- items_db: `213994`
- items_missing_in_db: `12`
- codes_upstream: `87183`
- codes_db: `258843`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261116_033925Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
