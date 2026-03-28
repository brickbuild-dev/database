# Brickovery DB backup & change audit — 20260328_010815Z

## Context
- created_at_utc: **20260328_010815Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `435` (id `23673994450`)
- commit: `55cb9dd2ada3677bcfea252cd6946f68090e5fe7`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `ef6c5913639e5db2a55e6b21f616da8f966e449e04cb137b4904fd907432adb2`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260328_010815Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260328_010815Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `5127943b9900e3311783aa80223f314f405cd2657364b9fa8181822114ab8df0`
- csv_size_bytes (pre-update): `26135442`
- csv_backup_file: `brickovery_db_csv_backup_20260328_010815Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `204535`
- items_db: `204611`
- items_missing_in_db: `20`
- codes_upstream: `84066`
- codes_db: `245051`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260328_010815Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
