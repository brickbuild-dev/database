# Brickovery DB backup & change audit — 20260425_013044Z

## Context
- created_at_utc: **20260425_013044Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2933` (id `24919229017`)
- commit: `95066baf9e16ba3539976765855890645ac79cd7`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `9994d2c218fd8ac4c2547a83ddd0b0267838646b935db3562db6ac8aa9359c08`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260425_013044Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260425_013044Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `c12c66773f7da1f1559c4d268d73673d43851b2125d189c03634b4eb79370ee0`
- csv_size_bytes (pre-update): `26206003`
- csv_backup_file: `brickovery_db_csv_backup_20260425_013044Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205285`
- items_db: `205653`
- items_missing_in_db: `1`
- codes_upstream: `84257`
- codes_db: `246277`
- codes_missing_in_db: `10`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260425_013044Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
