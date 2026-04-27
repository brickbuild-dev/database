# Brickovery DB backup & change audit — 20260427_013244Z

## Context
- created_at_utc: **20260427_013244Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2937` (id `24972275295`)
- commit: `33007296bf89f4ec1614120618e2f543496d0a1f`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `bd6445d9914f5fbc4dcef8c30622f7b83e63f7370453b411283fe38ba41e8704`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260427_013244Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260427_013244Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `63d6702b49afc1c0f8c810e1b5c2668f794caced1a287872e2da5e66ad044aba`
- csv_size_bytes (pre-update): `26207131`
- csv_backup_file: `brickovery_db_csv_backup_20260427_013244Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205352`
- items_db: `205662`
- items_missing_in_db: `64`
- codes_upstream: `84259`
- codes_db: `246297`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260427_013244Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
