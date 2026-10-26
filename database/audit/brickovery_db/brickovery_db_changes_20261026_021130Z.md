# Brickovery DB backup & change audit — 20261026_021130Z

## Context
- created_at_utc: **20261026_021130Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3806` (id `40257231421`)
- commit: `59caaa6792e2918a770a27e0cbad41a7ffea3821`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `7f7a21fe84f2b948fda20791b82f46c115b407c35608687caf106411d0a1715b`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261026_021130Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261026_021130Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e391db2c8fa3c7d9071a697f81d3f577f673f0780f6abe84dd8986481d884fda`
- csv_size_bytes (pre-update): `26901656`
- csv_backup_file: `brickovery_db_csv_backup_20261026_021130Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211828`
- items_db: `213660`
- items_missing_in_db: `36`
- codes_upstream: `87064`
- codes_db: `258381`
- codes_missing_in_db: `14`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261026_021130Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
