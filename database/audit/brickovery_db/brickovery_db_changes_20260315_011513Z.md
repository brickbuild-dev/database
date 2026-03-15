# Brickovery DB backup & change audit — 20260315_011513Z

## Context
- created_at_utc: **20260315_011513Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `393` (id `23100405508`)
- commit: `4ce0ca443c2480aed7677c82ca896d04e6d8d4ae`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `622d9aeb46b3775d6884d672cd0d596631bb79e63e9f6ec80c6132f265d92c80`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260315_011513Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260315_011513Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `a971eb883dd76ec4aefe16b8bf8f9952f50721bb3f679ec2ee12d966c5a76067`
- csv_size_bytes (pre-update): `26073287`
- csv_backup_file: `brickovery_db_csv_backup_20260315_011513Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203563`
- items_db: `203587`
- items_missing_in_db: `46`
- codes_upstream: `83961`
- codes_db: `243918`
- codes_missing_in_db: `11`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260315_011513Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
