# Brickovery DB backup & change audit — 20260614_023551Z

## Context
- created_at_utc: **20260614_023551Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3029` (id `27485944721`)
- commit: `68f1d79f555b1c8e700e060cb4a306078099ac93`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `8d6f8c68e0850f6e801135dbf8bd80f6e645e0ff6105d05113e1d0e03991c6b0`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260614_023551Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260614_023551Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `54b02bba0df08bfb2e3189fc77b1d6843f1c8b2b711eccd9ef34570c17d2bf78`
- csv_size_bytes (pre-update): `26383295`
- csv_backup_file: `brickovery_db_csv_backup_20260614_023551Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207054`
- items_db: `207397`
- items_missing_in_db: `264`
- codes_upstream: `84743`
- codes_db: `249340`
- codes_missing_in_db: `34`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260614_023551Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
