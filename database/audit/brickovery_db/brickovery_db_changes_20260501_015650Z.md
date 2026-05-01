# Brickovery DB backup & change audit — 20260501_015650Z

## Context
- created_at_utc: **20260501_015650Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2945` (id `25198468561`)
- commit: `5a5278da7db5b5860636e14c27f23cf9fe322043`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `4f87787b4815b04bf540d28cf1115a8a107c2144bc10e5a77d9cfffa306ef7b1`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260501_015650Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260501_015650Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `66548c1f6cdd23ef54eb2241c2bdfa0ebb37174ebdaea494d13ca3fcacf7e48c`
- csv_size_bytes (pre-update): `26224555`
- csv_backup_file: `brickovery_db_csv_backup_20260501_015650Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205393`
- items_db: `205763`
- items_missing_in_db: `4`
- codes_upstream: `84464`
- codes_db: `246598`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260501_015650Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
