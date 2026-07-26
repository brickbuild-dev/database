# Brickovery DB backup & change audit — 20260726_013524Z

## Context
- created_at_utc: **20260726_013524Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3178` (id `30182945104`)
- commit: `c576758f0b7e040a1467b35c29074955ba742e98`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `5528d8ed34a8792596d91689ddc1f49621b775fee22bc64398c930e5956c5793`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260726_013524Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260726_013524Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `33704cff15adf56d016b1b251311598ac4e2125299076d4d480cc92253946234`
- csv_size_bytes (pre-update): `26501510`
- csv_backup_file: `brickovery_db_csv_backup_20260726_013524Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `208102`
- items_db: `208762`
- items_missing_in_db: `46`
- codes_upstream: `85415`
- codes_db: `251401`
- codes_missing_in_db: `10`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260726_013524Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
