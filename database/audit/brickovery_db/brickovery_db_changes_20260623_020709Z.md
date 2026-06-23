# Brickovery DB backup & change audit — 20260623_020709Z

## Context
- created_at_utc: **20260623_020709Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3087` (id `27997002310`)
- commit: `eca76a0898093b4fab5489205ecba86e39950848`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `73add17bcea267cbf366cc58cdd672dd454a36c209d71b15f3ccd9de5a1cbb41`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260623_020709Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260623_020709Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `aa4f7b462d76b806f462b2b01c43c7f3b8d241379fadfdea6c2a58ad503ab84c`
- csv_size_bytes (pre-update): `26428798`
- csv_backup_file: `brickovery_db_csv_backup_20260623_020709Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207364`
- items_db: `207983`
- items_missing_in_db: `15`
- codes_upstream: `84944`
- codes_db: `250142`
- codes_missing_in_db: `7`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260623_020709Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
