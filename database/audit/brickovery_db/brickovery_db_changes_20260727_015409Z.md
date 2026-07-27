# Brickovery DB backup & change audit — 20260727_015409Z

## Context
- created_at_utc: **20260727_015409Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3180` (id `30230589879`)
- commit: `7fb004c21fb3d637613c2b4730f958fec43ce103`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `a872fd877049c217f0b32c238ce82c24605f4050879989cab92668eb7fa264af`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260727_015409Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260727_015409Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `dc9d83bc1bd9dac6efd6390c1f1535af1b7c6facf8b4efc72380ba7c140f3f32`
- csv_size_bytes (pre-update): `26504258`
- csv_backup_file: `brickovery_db_csv_backup_20260727_015409Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `208104`
- items_db: `208808`
- items_missing_in_db: `22`
- codes_upstream: `85416`
- codes_db: `251455`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260727_015409Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
