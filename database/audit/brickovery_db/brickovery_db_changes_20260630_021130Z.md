# Brickovery DB backup & change audit — 20260630_021130Z

## Context
- created_at_utc: **20260630_021130Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3101` (id `28415339684`)
- commit: `083662246708039d1ae2013fb9b30afc4f6c1a8d`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `a1a478d707d82fac2dc67bdcfa057b97ae8613a8e2b07a7c4af00d3d9f52d73d`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260630_021130Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260630_021130Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `2ea10daf344c9b22d56a3dd3c89a4e1e9c846be5f2139dc866661ba7aaf48662`
- csv_size_bytes (pre-update): `26451620`
- csv_backup_file: `brickovery_db_csv_backup_20260630_021130Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207559`
- items_db: `208221`
- items_missing_in_db: `14`
- codes_upstream: `85118`
- codes_db: `250533`
- codes_missing_in_db: `49`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260630_021130Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
