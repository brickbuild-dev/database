# Brickovery DB backup & change audit — 20260718_012435Z

## Context
- created_at_utc: **20260718_012435Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3163` (id `29624910409`)
- commit: `725ac3b1d8450b2cffa6b74cbd0f2cb5e29ac9cc`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `cf27b1dae613291b150596277c0b0eba988649f363f6ebf2f0492c5d936348b8`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260718_012435Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260718_012435Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `1b252a23536457e02980d3a357bf6fa2f01fb299841c2d7830e00b5445783a12`
- csv_size_bytes (pre-update): `26488652`
- csv_backup_file: `brickovery_db_csv_backup_20260718_012435Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207879`
- items_db: `208570`
- items_missing_in_db: `7`
- codes_upstream: `85368`
- codes_db: `251173`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260718_012435Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
