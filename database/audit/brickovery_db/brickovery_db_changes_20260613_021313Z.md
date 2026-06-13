# Brickovery DB backup & change audit — 20260613_021313Z

## Context
- created_at_utc: **20260613_021313Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3027` (id `27453402685`)
- commit: `fa0b0928261289cea387d215cd6a325a2430d1fc`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `5286ac34f27773cde21beda08bc00fffaa32c69cf7178fb1a185a1dc0770a6fd`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260613_021313Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260613_021313Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `ad5f51cf54cae69dfdc837cadc3b79828a1a6be1f82f86554da223c09caa4675`
- csv_size_bytes (pre-update): `26377958`
- csv_backup_file: `brickovery_db_csv_backup_20260613_021313Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206792`
- items_db: `207329`
- items_missing_in_db: `68`
- codes_upstream: `84706`
- codes_db: `249247`
- codes_missing_in_db: `27`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260613_021313Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
