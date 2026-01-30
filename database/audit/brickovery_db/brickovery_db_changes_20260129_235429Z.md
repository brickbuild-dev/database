# Brickovery DB backup & change audit — 20260129_235429Z

## Context
- created_at_utc: **20260129_235429Z**
- reason: **manual_force_rebuild**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `27` (id `21499038244`)
- commit: `53b3d77b7f8b0e895c31ed980fe632f6cf1f2aa3`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `663fa6f439351fe7e92743b7290849cdd6a8efde1602f7e2f21d07051f2ee301`
- db_size_bytes (pre-update): `41742336`
- backup_file: `brickovery_db_backup_20260129_235429Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260129_235429Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `6c8b8f4be32897bc5940fbdc40b825d6d8c7c141ecbb3da6f7a2903a2143e4cc`
- csv_size_bytes (pre-update): `15934712`
- csv_backup_file: `brickovery_db_csv_backup_20260129_235429Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202286`
- items_db: `245830`
- items_missing_in_db: `4`
- codes_upstream: `83242`
- codes_db: `325214`
- codes_missing_in_db: `4`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260129_235429Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
