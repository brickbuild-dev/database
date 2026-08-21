# Brickovery DB backup & change audit — 20260821_004021Z

## Context
- created_at_utc: **20260821_004021Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3230` (id `32433172884`)
- commit: `b213a47d625b0244dc902a4b027cd2b6a48249bb`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `30e148d88dc1df0a86b563fafd0b7d65b8bcad8ed282441debe2e18dbde5f506`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260821_004021Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260821_004021Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `50aea32a2218c26bdaa8a5445cb5a77290b4a6b599658d6f9b09a52f2fe77f15`
- csv_size_bytes (pre-update): `26645907`
- csv_backup_file: `brickovery_db_csv_backup_20260821_004021Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209767`
- items_db: `210464`
- items_missing_in_db: `99`
- codes_upstream: `86264`
- codes_db: `253949`
- codes_missing_in_db: `36`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260821_004021Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
