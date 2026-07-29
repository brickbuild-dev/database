# Brickovery DB backup & change audit — 20260729_012933Z

## Context
- created_at_utc: **20260729_012933Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3184` (id `30413863392`)
- commit: `b898e44606f645136c0727f79ad8dc8ba2c80ec4`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `eb5e31d5f12e03d5c08140755d81732f1bf5377be0d950631c930fa9313a921a`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260729_012933Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260729_012933Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `85bebd62936a17eb07c0221c1af3e5f08edf1fb544694dcae481cfb245924e76`
- csv_size_bytes (pre-update): `26506436`
- csv_backup_file: `brickovery_db_csv_backup_20260729_012933Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `208134`
- items_db: `208847`
- items_missing_in_db: `14`
- codes_upstream: `85417`
- codes_db: `251495`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260729_012933Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
