# Brickovery DB backup & change audit — 20261001_050740Z

## Context
- created_at_utc: **20261001_050740Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3560` (id `36817671753`)
- commit: `4cfa6ca69c6ec794fae86eaf9398b579003ee6e7`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `46af8a5cf5359be331f01f28cec5766437f34d2bf5c1b9a0394b2097d10b33a5`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261001_050740Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261001_050740Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `f37f1a8ee79b25bc4d8c7c7bab37abed6f5405f1cd1c9c6c58e777eebd4ee959`
- csv_size_bytes (pre-update): `26852552`
- csv_backup_file: `brickovery_db_csv_backup_20261001_050740Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211299`
- items_db: `213122`
- items_missing_in_db: `13`
- codes_upstream: `86738`
- codes_db: `257535`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261001_050740Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
