# Brickovery DB backup & change audit — 20260911_015345Z

## Context
- created_at_utc: **20260911_015345Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3378` (id `34552115796`)
- commit: `4d0daa60dc85a70587dfb27b53d8f9c7dcb858d4`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `557993491f82e6a9f1e2f31f620ea5bccd4fa2a4c00e6b15fe0c651634d9f0a6`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260911_015345Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260911_015345Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `3984e56c48e3d8899b6d7e0c6f89770bf95478b86804d45d6137615d967fb3ff`
- csv_size_bytes (pre-update): `26729438`
- csv_backup_file: `brickovery_db_csv_backup_20260911_015345Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210624`
- items_db: `211475`
- items_missing_in_db: `3`
- codes_upstream: `86616`
- codes_db: `255384`
- codes_missing_in_db: `7`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260911_015345Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
