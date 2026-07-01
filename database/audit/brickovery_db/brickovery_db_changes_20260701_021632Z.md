# Brickovery DB backup & change audit — 20260701_021632Z

## Context
- created_at_utc: **20260701_021632Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3103` (id `28488689626`)
- commit: `b22e53934aaa580d63d929d5c11b334a9fc61a33`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `ab70e19a4c0bd5b1797e35e03eab92a27e3d305f7f5d80634e9094c4a54e336c`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260701_021632Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260701_021632Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `47738856d0822bf2bb493904969eebf5862b1b5cc13bfacc529cdb3d4648d8fc`
- csv_size_bytes (pre-update): `26455186`
- csv_backup_file: `brickovery_db_csv_backup_20260701_021632Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207603`
- items_db: `208235`
- items_missing_in_db: `44`
- codes_upstream: `85136`
- codes_db: `250595`
- codes_missing_in_db: `17`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260701_021632Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
