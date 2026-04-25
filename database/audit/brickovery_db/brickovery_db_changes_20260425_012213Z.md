# Brickovery DB backup & change audit — 20260425_012213Z

## Context
- created_at_utc: **20260425_012213Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2932` (id `24919059709`)
- commit: `5a3298f6edda46709a1ed432af22e92b94e207dc`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `bb95340224c6988e8ceeb55305119b8bcc78cb56b12ccff95a7194ca9191e0f3`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260425_012213Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260425_012213Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `4ea2f13ebbde888fae1b0431f0f962dba58b8b061d73113f179b8d78985c0868`
- csv_size_bytes (pre-update): `26205723`
- csv_backup_file: `brickovery_db_csv_backup_20260425_012213Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205285`
- items_db: `205649`
- items_missing_in_db: `4`
- codes_upstream: `84247`
- codes_db: `246272`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260425_012213Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
