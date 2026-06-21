# Brickovery DB backup & change audit — 20260621_023659Z

## Context
- created_at_utc: **20260621_023659Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3083` (id `27891011528`)
- commit: `d27ca38a439d0827644eaf146aa10b619f020e54`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `6bf9eba38ed7b5f33943f1736d3044e9984b60bebe88d66d60b3f24ba11ca49b`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260621_023659Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260621_023659Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `7a6839d333eabffcec77fb16abec61534607cf77ed9ba29364dcbbcd77175686`
- csv_size_bytes (pre-update): `26425168`
- csv_backup_file: `brickovery_db_csv_backup_20260621_023659Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207343`
- items_db: `207958`
- items_missing_in_db: `19`
- codes_upstream: `84935`
- codes_db: `250082`
- codes_missing_in_db: `34`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260621_023659Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
