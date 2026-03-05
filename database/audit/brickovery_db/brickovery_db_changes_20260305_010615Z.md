# Brickovery DB backup & change audit — 20260305_010615Z

## Context
- created_at_utc: **20260305_010615Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `373` (id `22697268238`)
- commit: `cca2796810c28c63a3396841b22308fe50ed426e`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `c6e5c43e5ea7161538c25bf1705a1f9c25eaf59eb9089ad917387b281c94841b`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260305_010615Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260305_010615Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `abb8219257f42d1c1cc1293ffb2256ac4319db34e3d6df08f873f3c16416c63d`
- csv_size_bytes (pre-update): `26050267`
- csv_backup_file: `brickovery_db_csv_backup_20260305_010615Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203308`
- items_db: `203341`
- items_missing_in_db: `20`
- codes_upstream: `83794`
- codes_db: `243517`
- codes_missing_in_db: `13`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260305_010615Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
