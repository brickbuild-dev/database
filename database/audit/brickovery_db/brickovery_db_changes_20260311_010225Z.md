# Brickovery DB backup & change audit — 20260311_010225Z

## Context
- created_at_utc: **20260311_010225Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `385` (id `22931542440`)
- commit: `bc4db271bb781b8d2b2071ba4cbe971d0a80d138`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `eb95a463ad6e96f2da233e9cee5501dce62974268aed3648f89c4900681aa575`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260311_010225Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260311_010225Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `89ed4f79d1095d8bf52ef140934616a322a0ec1db326fbc3eeae7ddb43a73f44`
- csv_size_bytes (pre-update): `26066472`
- csv_backup_file: `brickovery_db_csv_backup_20260311_010225Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203461`
- items_db: `203493`
- items_missing_in_db: `28`
- codes_upstream: `83933`
- codes_db: `243799`
- codes_missing_in_db: `10`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260311_010225Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
