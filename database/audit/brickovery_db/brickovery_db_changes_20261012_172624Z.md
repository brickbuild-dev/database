# Brickovery DB backup & change audit — 20261012_172624Z

## Context
- created_at_utc: **20261012_172624Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3749` (id `38278573476`)
- commit: `5c7bfe6af6bbb9379f48ed3577d1bfc413bf497e`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `d1b0ee41c410c58b65b0357cfaac6b0968a3177b5ac659090f47adf5d5a8eb3b`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261012_172624Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261012_172624Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `274fff2ab6be473b18df9010fc6ae5c0d9aa09db6129230647e3fdb124445f80`
- csv_size_bytes (pre-update): `26884207`
- csv_backup_file: `brickovery_db_csv_backup_20261012_172624Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211597`
- items_db: `213439`
- items_missing_in_db: `10`
- codes_upstream: `86979`
- codes_db: `258077`
- codes_missing_in_db: `11`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261012_172624Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
