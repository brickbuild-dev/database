# Brickovery DB backup & change audit — 20260819_003927Z

## Context
- created_at_utc: **20260819_003927Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3226` (id `32201590236`)
- commit: `dff2e8f2850efe5f139e2ceec224ddc13907d722`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `b17cfeec20a5dad359cc21dd71cdc52f518e3398dac3a8b1e539b68815489f15`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260819_003927Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260819_003927Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `412fb4cb8f972eaa213471afc63cb7722126fcccdd23076cadeeb20e56164c21`
- csv_size_bytes (pre-update): `26645316`
- csv_backup_file: `brickovery_db_csv_backup_20260819_003927Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209672`
- items_db: `210457`
- items_missing_in_db: `5`
- codes_upstream: `86234`
- codes_db: `253939`
- codes_missing_in_db: `3`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260819_003927Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
