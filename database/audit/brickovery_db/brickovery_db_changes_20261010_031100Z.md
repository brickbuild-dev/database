# Brickovery DB backup & change audit — 20261010_031100Z

## Context
- created_at_utc: **20261010_031100Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3664` (id `38019256322`)
- commit: `1c785dbfe92df95f7cd9d9decff1ff82a2cf6c27`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `278e5e9ec424d358b3644641db4fa6967e0c35265f0672103f6fd75efa2f7548`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261010_031100Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261010_031100Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e0af80f3b2ed63222295d32adb6e49396d8b77c936c4d6e55c4f4ba494e3e02f`
- csv_size_bytes (pre-update): `26880149`
- csv_backup_file: `brickovery_db_csv_backup_20261010_031100Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211561`
- items_db: `213398`
- items_missing_in_db: `10`
- codes_upstream: `86953`
- codes_db: `258008`
- codes_missing_in_db: `13`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261010_031100Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
