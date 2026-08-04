# Brickovery DB backup & change audit — 20260804_012513Z

## Context
- created_at_utc: **20260804_012513Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3196` (id `30868325496`)
- commit: `501c03243712e9f3a006c53ca26c8d8ffde709d5`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `c9118ecf2307ca2cfb1732ed4a22a7b69cd66544db036f3952378862d10c16cd`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260804_012513Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260804_012513Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `30fe548d1461f4a4a6eee7d2eed3d3004da87e57e05cea253d2dd33ae06da5ca`
- csv_size_bytes (pre-update): `26593366`
- csv_backup_file: `brickovery_db_csv_backup_20260804_012513Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209097`
- items_db: `209836`
- items_missing_in_db: `25`
- codes_upstream: `85998`
- codes_db: `253033`
- codes_missing_in_db: `21`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260804_012513Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
