# Brickovery DB backup & change audit — 20260904_014951Z

## Context
- created_at_utc: **20260904_014951Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3283` (id `33826831586`)
- commit: `954a3052dc6ea39bb8ff8de133e634f92febadba`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `c9d980b87a14b4d20109e43918008b0aa6c8411ffa571369473687b5b9232928`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260904_014951Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260904_014951Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `de2132bd34818340a8b0b80033063858f1d090bb5d9fa10f36c7d6418d187418`
- csv_size_bytes (pre-update): `26690725`
- csv_backup_file: `brickovery_db_csv_backup_20260904_014951Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210226`
- items_db: `211025`
- items_missing_in_db: `37`
- codes_upstream: `86403`
- codes_db: `254712`
- codes_missing_in_db: `8`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260904_014951Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
