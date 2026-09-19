# Brickovery DB backup & change audit — 20260919_020649Z

## Context
- created_at_utc: **20260919_020649Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3394` (id `35414310421`)
- commit: `e72e5bee050e5a7cd713ce9a83d16ea8a9e18949`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `46d69c6473685a73d87686c295d18316367128101b208150e9ed388d562158b1`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260919_020649Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260919_020649Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `56cd5d557dd71c32ec0620b62cb936085d04d3d9fbcb629bbb38a440fb89db1a`
- csv_size_bytes (pre-update): `26744934`
- csv_backup_file: `brickovery_db_csv_backup_20260919_020649Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210788`
- items_db: `211653`
- items_missing_in_db: `3`
- codes_upstream: `86703`
- codes_db: `255648`
- codes_missing_in_db: `15`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260919_020649Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
