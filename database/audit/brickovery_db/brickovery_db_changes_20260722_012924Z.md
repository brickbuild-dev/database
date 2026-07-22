# Brickovery DB backup & change audit — 20260722_012924Z

## Context
- created_at_utc: **20260722_012924Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3170` (id `29882871875`)
- commit: `858463e37d86a0998b4800081ec3e9d808ce3cfd`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `4dba0b0e0ad8ca90818906e5e1e3453ea4836b08c2cea24f7750ead8be17edc3`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260722_012924Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260722_012924Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `f6446aae9998eb82d1a46e5f05f3acb1b45227a66af18ede9ea4f94615fb1dbe`
- csv_size_bytes (pre-update): `26499038`
- csv_backup_file: `brickovery_db_csv_backup_20260722_012924Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `208037`
- items_db: `208719`
- items_missing_in_db: `22`
- codes_upstream: `85405`
- codes_db: `251357`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260722_012924Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
