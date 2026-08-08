# Brickovery DB backup & change audit — 20260808_005111Z

## Context
- created_at_utc: **20260808_005111Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3204` (id `31230865149`)
- commit: `6f1d30fe064710b13134fdb16f7e327035c01cc2`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `555903df2bb8438721911be64c39845f7fda3549ac363974050b6b71e9673185`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260808_005111Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260808_005111Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `237546fcb127427a4126945dcd967907f72ecd398ee15d16fe6ec283a1c06e65`
- csv_size_bytes (pre-update): `26607736`
- csv_backup_file: `brickovery_db_csv_backup_20260808_005111Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209308`
- items_db: `210035`
- items_missing_in_db: `47`
- codes_upstream: `86012`
- codes_db: `253289`
- codes_missing_in_db: `19`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260808_005111Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
