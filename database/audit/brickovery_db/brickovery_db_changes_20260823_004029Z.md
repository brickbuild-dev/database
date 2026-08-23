# Brickovery DB backup & change audit — 20260823_004029Z

## Context
- created_at_utc: **20260823_004029Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3234` (id `32608196124`)
- commit: `586ec91d0b620a1c554f1b4990274c802f477546`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `d279d60c3251305c3010619fb309cf75cb326015deb427bd8e71033ad1a6e87b`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260823_004029Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260823_004029Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `19f192fdb54492c67507fbc10f7fb963d774d833f99f53e00696544e8ce01dbb`
- csv_size_bytes (pre-update): `26656494`
- csv_backup_file: `brickovery_db_csv_backup_20260823_004029Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209779`
- items_db: `210576`
- items_missing_in_db: `1`
- codes_upstream: `86304`
- codes_db: `254130`
- codes_missing_in_db: `5`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260823_004029Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
