# Brickovery DB backup & change audit — 20260606_020410Z

## Context
- created_at_utc: **20260606_020410Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3013` (id `27049412861`)
- commit: `3cae958fae7b28588a56213c11a5e6c3cb3ebb87`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `6a2ed8fc375dc6ad7b67b1e3c07c5c5d75ce085d64689a6699755e74a852c401`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260606_020410Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260606_020410Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `9954aa58ea6a1dff14fcb8e046831497a79bd9197c6ba98a1933eee4b7136da1`
- csv_size_bytes (pre-update): `26356588`
- csv_backup_file: `brickovery_db_csv_backup_20260606_020410Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206563`
- items_db: `207148`
- items_missing_in_db: `9`
- codes_upstream: `84478`
- codes_db: `248874`
- codes_missing_in_db: `9`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260606_020410Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
