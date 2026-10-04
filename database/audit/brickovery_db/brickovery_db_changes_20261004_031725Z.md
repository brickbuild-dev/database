# Brickovery DB backup & change audit — 20261004_031725Z

## Context
- created_at_utc: **20261004_031725Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3652` (id `37173277731`)
- commit: `b471854c92813b6aa85430babd031389996a34b0`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `c0f30e456edd5296ce88cde6e30a455a7f7d3466a9cadf229fa6217a7a1f03ad`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261004_031725Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261004_031725Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `45c290e0a829d26790d8793651b9cde3a54b3b374d530a45bb89444a9640a20e`
- csv_size_bytes (pre-update): `26859858`
- csv_backup_file: `brickovery_db_csv_backup_20261004_031725Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211435`
- items_db: `213237`
- items_missing_in_db: `33`
- codes_upstream: `86786`
- codes_db: `257660`
- codes_missing_in_db: `35`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261004_031725Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
