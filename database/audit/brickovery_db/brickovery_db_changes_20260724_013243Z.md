# Brickovery DB backup & change audit — 20260724_013243Z

## Context
- created_at_utc: **20260724_013243Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3174` (id `30058931541`)
- commit: `9a2257645c97257aadee6800b3ab10b787c3c77e`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `949f0541e5c88b2d1259b3f57cd1b03f00b9cc02077b5995930cc6f956d0236f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260724_013243Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260724_013243Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `3b751597330a4f3f64d4d79bcc94febb76d4c18d80beede757a367ee0079c20c`
- csv_size_bytes (pre-update): `26500900`
- csv_backup_file: `brickovery_db_csv_backup_20260724_013243Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `208057`
- items_db: `208751`
- items_missing_in_db: `10`
- codes_upstream: `85406`
- codes_db: `251390`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260724_013243Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
