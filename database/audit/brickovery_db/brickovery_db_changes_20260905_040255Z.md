# Brickovery DB backup & change audit — 20260905_040255Z

## Context
- created_at_utc: **20260905_040255Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3347` (id `33943142767`)
- commit: `dcc6e4ad84248a14581edc63b2da745b6f6385d2`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `664e1a57330ce699cecb508918279d7340fb8cc3d794a790f4c1b60f313e2211`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260905_040255Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260905_040255Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `4dba080975409b0ef9097530f79fd4521d7250ea4eacb37793469884227aa64e`
- csv_size_bytes (pre-update): `26697375`
- csv_backup_file: `brickovery_db_csv_backup_20260905_040255Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210287`
- items_db: `211119`
- items_missing_in_db: `4`
- codes_upstream: `86414`
- codes_db: `254825`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260905_040255Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
