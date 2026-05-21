# Brickovery DB backup & change audit — 20260521_020736Z

## Context
- created_at_utc: **20260521_020736Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2981` (id `26201015710`)
- commit: `0492b5074888257463fab4c3249c91052bacd9e8`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `d84da4b51b257d88f2d5f95b17a112ee34f72af3da1fc85b1030980603e67fda`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260521_020736Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260521_020736Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `a5d45e248699bcd11cc94f1d75f3a635b51323c72b13c5362f60af6b61afef07`
- csv_size_bytes (pre-update): `26304936`
- csv_backup_file: `brickovery_db_csv_backup_20260521_020736Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205905`
- items_db: `206397`
- items_missing_in_db: `35`
- codes_upstream: `84388`
- codes_db: `247987`
- codes_missing_in_db: `50`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260521_020736Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
