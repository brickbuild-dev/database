# Brickovery DB backup & change audit — 20260326_011448Z

## Context
- created_at_utc: **20260326_011448Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `415` (id `23572514281`)
- commit: `0276eebf194fac2edda6bfe11e50e64e761056ea`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `c9f7d60f192e3f94a265825829fdd68a797019f3ebd5055261d1a976a321702d`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260326_011448Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260326_011448Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `ae18dd88ed29986761ca184f4a759ef9de8c7dccedbec67fac78b5a78e23b60e`
- csv_size_bytes (pre-update): `26095033`
- csv_backup_file: `brickovery_db_csv_backup_20260326_011448Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `204110`
- items_db: `203874`
- items_missing_in_db: `330`
- codes_upstream: `84054`
- codes_db: `244302`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260326_011448Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
