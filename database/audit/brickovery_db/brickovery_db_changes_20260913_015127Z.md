# Brickovery DB backup & change audit — 20260913_015127Z

## Context
- created_at_utc: **20260913_015127Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3382` (id `34731345083`)
- commit: `d9a6ce225b155ea48aecaa4d9846caeb151c8a3d`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `741b0f3936fd2e4ef7f1b457c93d78ad659b6e882909bc9c0c7b9e987b1c5f1c`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260913_015127Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260913_015127Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `dd3f75ff215494904f2baa09cd11f4972b92c88c52624f7a4c5a96fd07347433`
- csv_size_bytes (pre-update): `26732653`
- csv_backup_file: `brickovery_db_csv_backup_20260913_015127Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210675`
- items_db: `211516`
- items_missing_in_db: `20`
- codes_upstream: `86640`
- codes_db: `255440`
- codes_missing_in_db: `17`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260913_015127Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
