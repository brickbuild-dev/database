# Brickovery DB backup & change audit — 20260818_003845Z

## Context
- created_at_utc: **20260818_003845Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3224` (id `32084844321`)
- commit: `40288cb13d319b214211ca1ad8dd0f02d4b5ad0e`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `c720707de4eaca7a66b5b7f81cc9ddafc1457c1500e9bd9841ab0562f3a042c4`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260818_003845Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260818_003845Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `f9ccac8e3a7a3d140fa1518327dc8f852a49dad83ca946866e26ded24fc224bf`
- csv_size_bytes (pre-update): `26645096`
- csv_backup_file: `brickovery_db_csv_backup_20260818_003845Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209670`
- items_db: `210453`
- items_missing_in_db: `4`
- codes_upstream: `86234`
- codes_db: `253935`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260818_003845Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
