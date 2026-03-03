# Brickovery DB backup & change audit — 20260303_010745Z

## Context
- created_at_utc: **20260303_010745Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `369` (id `22603392389`)
- commit: `c1e8a98ad1ff826e853b8139569cb1043b164c39`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `486209a02fb89e13d92605254830e962e61ce009be61e273b8d3d9056aaa2095`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260303_010745Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260303_010745Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `7f7f8a95ee8a1d34a9ae74cb244de6bf6c752cbdd2cdc0dce251735daa679c2e`
- csv_size_bytes (pre-update): `26043053`
- csv_backup_file: `brickovery_db_csv_backup_20260303_010745Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203277`
- items_db: `203268`
- items_missing_in_db: `58`
- codes_upstream: `83757`
- codes_db: `243393`
- codes_missing_in_db: `31`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260303_010745Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
