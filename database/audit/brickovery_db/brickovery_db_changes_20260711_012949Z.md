# Brickovery DB backup & change audit — 20260711_012949Z

## Context
- created_at_utc: **20260711_012949Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3122` (id `29134528022`)
- commit: `51651629ff494b20b50166625a498c445f9c47f6`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `6ecbf91dbdf1a395840bcc63ea8075433a813704d049915d48ada8f7b86a414b`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260711_012949Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260711_012949Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `19327d97a260a2afe745a561409068289f23f082b557272c9b873cb4380f2b5d`
- csv_size_bytes (pre-update): `26479606`
- csv_backup_file: `brickovery_db_csv_backup_20260711_012949Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207826`
- items_db: `208504`
- items_missing_in_db: `3`
- codes_upstream: `85287`
- codes_db: `251015`
- codes_missing_in_db: `13`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260711_012949Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
