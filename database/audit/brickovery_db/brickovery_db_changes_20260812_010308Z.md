# Brickovery DB backup & change audit — 20260812_010308Z

## Context
- created_at_utc: **20260812_010308Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3212` (id `31551863333`)
- commit: `a2a52da254a6b5280f9f7bbb5ae70ac03403f632`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `5ca285b82647a610928925edbfb851154b905eb060974999e0ea59b568ac1fe0`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260812_010308Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260812_010308Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `013e573eaa1dfb24a4c3bc6aab7235e4c967592e9385f64ba8c17c9af0c2e552`
- csv_size_bytes (pre-update): `26621379`
- csv_backup_file: `brickovery_db_csv_backup_20260812_010308Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209484`
- items_db: `210223`
- items_missing_in_db: `39`
- codes_upstream: `86074`
- codes_db: `253527`
- codes_missing_in_db: `29`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260812_010308Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
