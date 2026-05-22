# Brickovery DB backup & change audit — 20260522_021026Z

## Context
- created_at_utc: **20260522_021026Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2983` (id `26264151022`)
- commit: `f3c92a3912cc0ffb6541901098db325cab89c516`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `dc67d31b9b976c54d9cd8e7f701abff0c9e15bfeb82c2f4eff7a768f40dd6706`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260522_021026Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260522_021026Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `9c15c4ef1d3499a76c484b830ae14d8133a441c0e653bad3fd11bc60f1fa4694`
- csv_size_bytes (pre-update): `26309634`
- csv_backup_file: `brickovery_db_csv_backup_20260522_021026Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205915`
- items_db: `206432`
- items_missing_in_db: `20`
- codes_upstream: `84398`
- codes_db: `248072`
- codes_missing_in_db: `23`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260522_021026Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
