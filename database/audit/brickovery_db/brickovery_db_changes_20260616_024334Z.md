# Brickovery DB backup & change audit — 20260616_024334Z

## Context
- created_at_utc: **20260616_024334Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3034` (id `27590230497`)
- commit: `07ac2c1054ada45ac261bc4bd0e76611405bddd9`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `368222822f03ddcdcb21faae81576a7b1deb2cea131fdc55a7212d9b03a04476`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260616_024334Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260616_024334Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `cb0db65eed212613f0e37d41556fdbf0946e4c42a8ed43f9cd38b590ad9eec26`
- csv_size_bytes (pre-update): `26407760`
- csv_backup_file: `brickovery_db_csv_backup_20260616_024334Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207204`
- items_db: `207757`
- items_missing_in_db: `64`
- codes_upstream: `84849`
- codes_db: `249780`
- codes_missing_in_db: `59`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260616_024334Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
