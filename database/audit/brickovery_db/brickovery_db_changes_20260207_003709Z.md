# Brickovery DB backup & change audit — 20260207_003709Z

## Context
- created_at_utc: **20260207_003709Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `121` (id `21770851632`)
- commit: `10737c380b27cf73cb6625cae29fdfd0266daf12`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `83ca0090b63772750af167f9d2acd98fc5bd902a735d16a9c2991e1dc1458af9`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260207_003709Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260207_003709Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `c896aa56c64d58dd825076e31169c1aa24c5ea60bcc5df93234b9848f24e48de`
- csv_size_bytes (pre-update): `25502187`
- csv_backup_file: `brickovery_db_csv_backup_20260207_003709Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202411`
- items_db: `202403`
- items_missing_in_db: `8`
- codes_upstream: `83290`
- codes_db: `242096`
- codes_missing_in_db: `7`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260207_003709Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
