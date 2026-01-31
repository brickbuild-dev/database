# Brickovery DB backup & change audit — 20260131_013722Z

## Context
- created_at_utc: **20260131_013722Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync upstream + update brickovery DB (semantic + chunked rebuild)`
- run: `40` (id `21536503406`)
- commit: `73e5d51b046078d6fc7c744c854b966ad073dbaf`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `4ee02bd87060376b0c2e40ef4ed176126633e16a3ed99ce68e27ce4401c41b69`
- db_size_bytes (pre-update): `44376064`
- backup_file: `brickovery_db_backup_20260131_013722Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260131_013722Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e06e2cc32a4318461c20c9f3fa53582d7085fe70f1cfc39412a2f4733881d6be`
- csv_size_bytes (pre-update): `16153392`
- csv_backup_file: `brickovery_db_csv_backup_20260131_013722Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202331`
- items_db: `237863`
- items_missing_in_db: `8`
- codes_upstream: `83259`
- codes_db: `282460`
- codes_missing_in_db: `16`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260131_013722Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
