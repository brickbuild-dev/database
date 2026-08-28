# Brickovery DB backup & change audit — 20260828_073024Z

## Context
- created_at_utc: **20260828_073024Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3244` (id `33151295586`)
- commit: `bb6e8b3dd6782a263731e394f00328b1e912a83b`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `2125515f8bd2edd29d697f5bf59758ed7140fcba4a4e7b792323901c33916ea1`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260828_073024Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260828_073024Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `7c066c7436f4686358981321a0611c2e08b5a78031873aa71c1b3b8295e2c498`
- csv_size_bytes (pre-update): `26667698`
- csv_backup_file: `brickovery_db_csv_backup_20260828_073024Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209889`
- items_db: `210691`
- items_missing_in_db: `13`
- codes_upstream: `86365`
- codes_db: `254321`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260828_073024Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
