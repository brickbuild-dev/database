# Brickovery DB backup & change audit — 20260604_023813Z

## Context
- created_at_utc: **20260604_023813Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3009` (id `26926520420`)
- commit: `ac9b278e9ee6d6db61c211cc035c319f36dcd3ef`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `308648052e44c4cd90298b6e4548555b3d1498de4a4342fdde2967916bc248f2`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260604_023813Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260604_023813Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `09421e88bb72b5cd7957d087171b9c65ae7a42ef8cbedb3ca3af4ebc82ddeef7`
- csv_size_bytes (pre-update): `26351738`
- csv_backup_file: `brickovery_db_csv_backup_20260604_023813Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206529`
- items_db: `207093`
- items_missing_in_db: `27`
- codes_upstream: `84454`
- codes_db: `248791`
- codes_missing_in_db: `16`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260604_023813Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
