# Brickovery DB backup & change audit — 20260914_021016Z

## Context
- created_at_utc: **20260914_021016Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3384` (id `34797909499`)
- commit: `917a157e992329be6b690bc6cd71e4988d500aa0`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `1401081e78926aa0889c7b35d3ede54ab5676ca4c8db072d45fdbe8e1e7febb5`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260914_021016Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260914_021016Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `bbcb0b419d811f8a93aafcfe86b1be9af0a8d62beab52569edc5b1940adbe134`
- csv_size_bytes (pre-update): `26734842`
- csv_backup_file: `brickovery_db_csv_backup_20260914_021016Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210691`
- items_db: `211536`
- items_missing_in_db: `17`
- codes_upstream: `86653`
- codes_db: `255477`
- codes_missing_in_db: `15`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260914_021016Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
