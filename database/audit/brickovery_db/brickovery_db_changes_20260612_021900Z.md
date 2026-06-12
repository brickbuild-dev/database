# Brickovery DB backup & change audit — 20260612_021900Z

## Context
- created_at_utc: **20260612_021900Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3025` (id `27390064140`)
- commit: `dc030365a4447936dee67103cab16518a9addd73`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `68483ee53027460acdba204d00918dfe4f1f7552c95c0438eb36397415356855`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260612_021900Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260612_021900Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `c813b870969dd6cec1f3c16ffe6dc81d706f2c7316eb9e4d578409302a39f467`
- csv_size_bytes (pre-update): `26376080`
- csv_backup_file: `brickovery_db_csv_backup_20260612_021900Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206729`
- items_db: `207309`
- items_missing_in_db: `20`
- codes_upstream: `84679`
- codes_db: `249214`
- codes_missing_in_db: `13`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260612_021900Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
