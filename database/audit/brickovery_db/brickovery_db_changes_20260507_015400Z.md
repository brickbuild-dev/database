# Brickovery DB backup & change audit — 20260507_015400Z

## Context
- created_at_utc: **20260507_015400Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2957` (id `25471373289`)
- commit: `b336fd4d5411e523c3115798737a9ad8a8f2e2ba`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `07cce64c1b3b3250ed54565f14c75f8348b0c874fe649608d40cfb931db7a2bd`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260507_015400Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260507_015400Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `7d6fc03a67292134540980504338ab2c431e15954d37a7f7a6716f28833c90a0`
- csv_size_bytes (pre-update): `26270304`
- csv_backup_file: `brickovery_db_csv_backup_20260507_015400Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205691`
- items_db: `206089`
- items_missing_in_db: `38`
- codes_upstream: `84953`
- codes_db: `247388`
- codes_missing_in_db: `91`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260507_015400Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
