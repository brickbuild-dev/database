# Brickovery DB backup & change audit — 20260928_022332Z

## Context
- created_at_utc: **20260928_022332Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3540` (id `36369270184`)
- commit: `be8d88bb06a621b475bd5e569fb601fda2885648`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `38c2210e0f67101dcbd1f191a26cba56398cbc88f8ca0275652d0e99cdf6cf36`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260928_022332Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260928_022332Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `82115fccdf218498507b2f28c0dccbb3f03179111f608baac85af6be7e8d340f`
- csv_size_bytes (pre-update): `26768709`
- csv_backup_file: `brickovery_db_csv_backup_20260928_022332Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211223`
- items_db: `212077`
- items_missing_in_db: `74`
- codes_upstream: `86711`
- codes_db: `256096`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260928_022332Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
