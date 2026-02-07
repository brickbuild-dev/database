# Brickovery DB backup & change audit — 20260207_145956Z

## Context
- created_at_utc: **20260207_145956Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `143` (id `21781981195`)
- commit: `c76b1196044ce704a6faf06ebb615e790d908df9`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `f7f4c1768b32bfe012b5167dbe672532f0cd10de93c53285f6e4368138ff226d`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260207_145956Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260207_145956Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `bdd293819ee1bee37c7ae9abf3667fca8128c5a98d9ac3a64e410a158a9e56b1`
- csv_size_bytes (pre-update): `25969708`
- csv_backup_file: `brickovery_db_csv_backup_20260207_145956Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202415`
- items_db: `202416`
- items_missing_in_db: `1`
- codes_upstream: `83290`
- codes_db: `242116`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260207_145956Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
