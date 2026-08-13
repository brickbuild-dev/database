# Brickovery DB backup & change audit — 20260813_010349Z

## Context
- created_at_utc: **20260813_010349Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3214` (id `31656099521`)
- commit: `d3925defcff8b4e4c8be5d527b59370f305c01e1`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `96659ec066fadc6748396c29ffad00b014e9e3b73bb3a131bb531c61206c95d1`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260813_010349Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260813_010349Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `4a8ed236ae00a183c210577018e445741b3b463e6ee38b39d6c259a74e4b7686`
- csv_size_bytes (pre-update): `26625139`
- csv_backup_file: `brickovery_db_csv_backup_20260813_010349Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209554`
- items_db: `210262`
- items_missing_in_db: `72`
- codes_upstream: `86126`
- codes_db: `253593`
- codes_missing_in_db: `55`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260813_010349Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
