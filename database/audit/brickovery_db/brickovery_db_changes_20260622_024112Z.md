# Brickovery DB backup & change audit — 20260622_024112Z

## Context
- created_at_utc: **20260622_024112Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3085` (id `27925979872`)
- commit: `340160da6c84638aeec242064b0dd130eb712677`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `7f1fedb735b597d3d651680abe87583f7f234b5e47a1f8957891ddb2a41e05d0`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260622_024112Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260622_024112Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `c36cffd18521010d7408421f7eb0ff14e3f34a9df0a65bcc904a719912dfdfc4`
- csv_size_bytes (pre-update): `26428385`
- csv_backup_file: `brickovery_db_csv_backup_20260622_024112Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207349`
- items_db: `207977`
- items_missing_in_db: `6`
- codes_upstream: `84937`
- codes_db: `250135`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260622_024112Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
