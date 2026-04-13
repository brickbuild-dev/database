# Brickovery DB backup & change audit — 20260413_012746Z

## Context
- created_at_utc: **20260413_012746Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2888` (id `24321366901`)
- commit: `4494ea03497e06583a769d649881985bb0ae7c9e`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `25fb541c9e35100928cb1aefcd2140ac7d65afcbb0759877b8eeebbf45406412`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260413_012746Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260413_012746Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8c6a3c91fdf0b1e7c589731f40b247a475fb43fcf23f584bcdaf1c420f6ae80f`
- csv_size_bytes (pre-update): `26191974`
- csv_backup_file: `brickovery_db_csv_backup_20260413_012746Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205183`
- items_db: `205524`
- items_missing_in_db: `7`
- codes_upstream: `84145`
- codes_db: `246032`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260413_012746Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
