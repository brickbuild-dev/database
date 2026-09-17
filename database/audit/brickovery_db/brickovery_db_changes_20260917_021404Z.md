# Brickovery DB backup & change audit — 20260917_021404Z

## Context
- created_at_utc: **20260917_021404Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3390` (id `35173179703`)
- commit: `0b99ea529b8a0a0884f5205d1221c9d2c6453282`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `a850b215c21331ee3ee130e14519b2ea1e55e011177b022bd2b32a484bfdd525`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260917_021404Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260917_021404Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `04b0b113b5af6d3687394b4ddaae820574476fc401e7c2452672d8cf21157ccd`
- csv_size_bytes (pre-update): `26743882`
- csv_backup_file: `brickovery_db_csv_backup_20260917_021404Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210780`
- items_db: `211643`
- items_missing_in_db: `4`
- codes_upstream: `86684`
- codes_db: `255630`
- codes_missing_in_db: `4`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260917_021404Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
