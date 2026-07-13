# Brickovery DB backup & change audit — 20260713_013328Z

## Context
- created_at_utc: **20260713_013328Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3129` (id `29217416347`)
- commit: `99015028a08646ee8fdcae35dc6e35d2c07cdb50`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `d4bebba4ae8d3379f4c3532047363a2035b30e21b6343fe10bad1f482067c274`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260713_013328Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260713_013328Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `58214ddc319942abee51ddb09e7551a126af0c4b9ece526624c0dde8c233c95b`
- csv_size_bytes (pre-update): `26480511`
- csv_backup_file: `brickovery_db_csv_backup_20260713_013328Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207842`
- items_db: `208507`
- items_missing_in_db: `24`
- codes_upstream: `85355`
- codes_db: `251031`
- codes_missing_in_db: `73`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260713_013328Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
