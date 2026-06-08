# Brickovery DB backup & change audit — 20260608_023629Z

## Context
- created_at_utc: **20260608_023629Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3017` (id `27112664293`)
- commit: `9824be2aa5e52416926ff782eca812ba434e6ec4`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `04da2017bab8683e574e96213ceef91ca9bb1aeeee2a500e84302acfc04e8c9f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260608_023629Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260608_023629Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d1a77b865c84409065a40ce64592843b8a014da8245a0a4b8efdd85277350adb`
- csv_size_bytes (pre-update): `26362436`
- csv_backup_file: `brickovery_db_csv_backup_20260608_023629Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206636`
- items_db: `207203`
- items_missing_in_db: `29`
- codes_upstream: `84569`
- codes_db: `248976`
- codes_missing_in_db: `47`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260608_023629Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
