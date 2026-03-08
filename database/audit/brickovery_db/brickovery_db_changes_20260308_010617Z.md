# Brickovery DB backup & change audit — 20260308_010617Z

## Context
- created_at_utc: **20260308_010617Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `379` (id `22810951860`)
- commit: `f8313837bbeda87ad9b6a6799c1c99c5f19068c6`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `1f8daa9f2867e724f98f4e32df889c179edd186b0dd95f20b0fb0d9bb3d69f8b`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260308_010617Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260308_010617Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `df4cbe2236badfe7f9ee14a71bdc16a6ce3ea9f83116d86780ea30ef079d0622`
- csv_size_bytes (pre-update): `26056624`
- csv_backup_file: `brickovery_db_csv_backup_20260308_010617Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203390`
- items_db: `203402`
- items_missing_in_db: `43`
- codes_upstream: `83862`
- codes_db: `243628`
- codes_missing_in_db: `29`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260308_010617Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
