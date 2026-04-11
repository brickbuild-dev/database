# Brickovery DB backup & change audit — 20260411_072156Z

## Context
- created_at_utc: **20260411_072156Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2884` (id `24277463917`)
- commit: `ca3dec0fb9a44f3dd3a23cadeb0d8a3b3ce2936a`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `432d2f194ceb0e7b735490b8eafd00ee084540f868cb3a80b4a77f264f869eb3`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260411_072156Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260411_072156Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e3d002b7653e5223ccaf91e4a56c201ec93a11f304082dda45d1ef72f2351fa1`
- csv_size_bytes (pre-update): `26190588`
- csv_backup_file: `brickovery_db_csv_backup_20260411_072156Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205173`
- items_db: `205508`
- items_missing_in_db: `2`
- codes_upstream: `84139`
- codes_db: `246007`
- codes_missing_in_db: `5`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260411_072156Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
