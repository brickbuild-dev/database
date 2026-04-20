# Brickovery DB backup & change audit — 20260420_012943Z

## Context
- created_at_utc: **20260420_012943Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2922` (id `24644116130`)
- commit: `8df0a9cfa486fb67a82cefacfbb46c49bb8f73a2`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `ff3df0d46451da2d644ee57e47d58ddc8637e6123feaa770ca54d723a2835087`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260420_012943Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260420_012943Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `289e13da2f72ea50aad41f8351e26b7677597d9070615bf5188f1e480b99ce48`
- csv_size_bytes (pre-update): `26196913`
- csv_backup_file: `brickovery_db_csv_backup_20260420_012943Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205256`
- items_db: `205593`
- items_missing_in_db: `22`
- codes_upstream: `84170`
- codes_db: `246118`
- codes_missing_in_db: `8`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260420_012943Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
