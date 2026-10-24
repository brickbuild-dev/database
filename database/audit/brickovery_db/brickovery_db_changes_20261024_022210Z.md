# Brickovery DB backup & change audit — 20261024_022210Z

## Context
- created_at_utc: **20261024_022210Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3802` (id `40053439113`)
- commit: `f8bb74269022e952791fc60b014168f3963c7e09`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `436e81630a59832f6cda3676665b732257ab344a7ca64884d5389d2adc70f3f8`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261024_022210Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261024_022210Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `22fdb44d3cf350e886af6d6f47e695bde1e11b805df3e8a9a4e6d8ee01487812`
- csv_size_bytes (pre-update): `26898814`
- csv_backup_file: `brickovery_db_csv_backup_20261024_022210Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211767`
- items_db: `213629`
- items_missing_in_db: `5`
- codes_upstream: `87032`
- codes_db: `258332`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261024_022210Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
