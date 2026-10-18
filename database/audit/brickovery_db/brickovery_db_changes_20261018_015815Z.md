# Brickovery DB backup & change audit — 20261018_015815Z

## Context
- created_at_utc: **20261018_015815Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3761` (id `39087994431`)
- commit: `1bb9b6b51ac21d11fe50fef50b80b89e3c428ce0`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `e27efdc2a683265c197e00e0a020b11810e1ca78a3f4984b73d4b730412d876a`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261018_015815Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261018_015815Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `c6e82cfe46526b97c7302af5ac6f4d9b28efa4019c946864a7d308612e496a1d`
- csv_size_bytes (pre-update): `26889440`
- csv_backup_file: `brickovery_db_csv_backup_20261018_015815Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211652`
- items_db: `213493`
- items_missing_in_db: `17`
- codes_upstream: `87005`
- codes_db: `258167`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261018_015815Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
