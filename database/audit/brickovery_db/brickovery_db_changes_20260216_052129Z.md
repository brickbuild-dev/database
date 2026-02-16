# Brickovery DB backup & change audit — 20260216_052129Z

## Context
- created_at_utc: **20260216_052129Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `346` (id `22051087335`)
- commit: `b92e0dad5a417c34f2429a9ea2b4ef3e7c052cb7`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `068bc7b8ac1cc4ca16aa11bea9dacf58aae37012e0d50eb9a1e9896a1ae9031e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260216_052129Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260216_052129Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `23bc17f459f32b089b000b6eefe1dca271010ced58f1c99777dabd896fe49d02`
- csv_size_bytes (pre-update): `25976355`
- csv_backup_file: `brickovery_db_csv_backup_20260216_052129Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202494`
- items_db: `202489`
- items_missing_in_db: `11`
- codes_upstream: `83337`
- codes_db: `242230`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260216_052129Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
