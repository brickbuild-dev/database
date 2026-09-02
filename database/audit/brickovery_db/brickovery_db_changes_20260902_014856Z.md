# Brickovery DB backup & change audit — 20260902_014856Z

## Context
- created_at_utc: **20260902_014856Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3254` (id `33580509423`)
- commit: `bbddefd92c88726c7be375ec2d09de0639858db7`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `9a75658db54f2f19fd800d6605928bc9531e7347e159a079014493ae45ec004c`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260902_014856Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260902_014856Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `268eae1b2c5ad92e97f76f2090dd938d4c3546f5a9d7c7df2ee7a4802e3da73f`
- csv_size_bytes (pre-update): `26672314`
- csv_backup_file: `brickovery_db_csv_backup_20260902_014856Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210129`
- items_db: `210745`
- items_missing_in_db: `205`
- codes_upstream: `86366`
- codes_db: `254400`
- codes_missing_in_db: `10`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260902_014856Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
