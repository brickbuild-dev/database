# Brickovery DB backup & change audit — 20261018_071124Z

## Context
- created_at_utc: **20261018_071124Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3790` (id `39106234305`)
- commit: `1f2436f0092607686b059717ad0644965ea6cb00`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `69e6809bfb6d45197aa3ed516ee486bb60faa7b0acbb25d48b45cec6900f631e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261018_071124Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261018_071124Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e03d655e42d2ec609650008698d3f8f0624c352c18ecad3cf70c12701bbe1c21`
- csv_size_bytes (pre-update): `26890569`
- csv_backup_file: `brickovery_db_csv_backup_20261018_071124Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211653`
- items_db: `213510`
- items_missing_in_db: `5`
- codes_upstream: `87005`
- codes_db: `258186`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261018_071124Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
