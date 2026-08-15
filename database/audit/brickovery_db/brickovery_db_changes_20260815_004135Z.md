# Brickovery DB backup & change audit — 20260815_004135Z

## Context
- created_at_utc: **20260815_004135Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3218` (id `31853944936`)
- commit: `941710f48f5619807e02defc36c8bd067cc604fc`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `4990efb0af5892cd3eb9e58a32c68108f3ef68b791bd27241e3cd25c4c905a61`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260815_004135Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260815_004135Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `28dd742b137404fc184e7783d8c679b062f0174cdc89ed068810abc840c39bb7`
- csv_size_bytes (pre-update): `26633396`
- csv_backup_file: `brickovery_db_csv_backup_20260815_004135Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209594`
- items_db: `210337`
- items_missing_in_db: `38`
- codes_upstream: `86174`
- codes_db: `253734`
- codes_missing_in_db: `30`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260815_004135Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
