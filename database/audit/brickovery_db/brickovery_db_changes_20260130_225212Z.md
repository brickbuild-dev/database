# Brickovery DB backup & change audit — 20260130_225212Z

## Context
- created_at_utc: **20260130_225212Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync upstream + update brickovery DB (semantic + chunked rebuild)`
- run: `39` (id `21533426985`)
- commit: `f8703b4a1487eb563e2659b24385a9b6bc41377c`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `663fa6f439351fe7e92743b7290849cdd6a8efde1602f7e2f21d07051f2ee301`
- db_size_bytes (pre-update): `41742336`
- backup_file: `brickovery_db_backup_20260130_225212Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260130_225212Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `6c8b8f4be32897bc5940fbdc40b825d6d8c7c141ecbb3da6f7a2903a2143e4cc`
- csv_size_bytes (pre-update): `15934712`
- csv_backup_file: `brickovery_db_csv_backup_20260130_225212Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202324`
- items_db: `245830`
- items_missing_in_db: `45`
- codes_upstream: `83243`
- codes_db: `325214`
- codes_missing_in_db: `5`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260130_225212Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
