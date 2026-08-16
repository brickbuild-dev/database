# Brickovery DB backup & change audit — 20260816_004101Z

## Context
- created_at_utc: **20260816_004101Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3220` (id `31917505097`)
- commit: `f4344342eee795adb3404169bf3802f380c8a184`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `aa1a61a1bf169a8a163a0cfd6741c91c135d4f4840fb16e8a52a867bce410849`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260816_004101Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260816_004101Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `23b96ecc8a59605860fa52c1c927adbb8c0b6af9e54860d0dd8e2fc494e9709a`
- csv_size_bytes (pre-update): `26637198`
- csv_backup_file: `brickovery_db_csv_backup_20260816_004101Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209639`
- items_db: `210375`
- items_missing_in_db: `47`
- codes_upstream: `86201`
- codes_db: `253799`
- codes_missing_in_db: `28`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260816_004101Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
