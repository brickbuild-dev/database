# Brickovery DB backup & change audit — 20260426_013121Z

## Context
- created_at_utc: **20260426_013121Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2935` (id `24945219004`)
- commit: `27a8214b3d3a68b5d325b53280be78a0c244cd32`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `e550aa92c3a0f80b88dca99299b7301425987ad6259fd4f0abbbd2c2e68edea2`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260426_013121Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260426_013121Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `205a1bf23f2dfe752cdd10a626900a1f0cd9a642aeff22e945f278e5fd366375`
- csv_size_bytes (pre-update): `26206622`
- csv_backup_file: `brickovery_db_csv_backup_20260426_013121Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205290`
- items_db: `205654`
- items_missing_in_db: `8`
- codes_upstream: `84259`
- codes_db: `246288`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260426_013121Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
