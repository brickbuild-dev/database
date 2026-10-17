# Brickovery DB backup & change audit — 20261017_015831Z

## Context
- created_at_utc: **20261017_015831Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3759` (id `38992709041`)
- commit: `58c8dba0f485ae9c1acb59b976d81946142db436`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `834baae6adac10b8f8f567c3725c8bdf58777599d59947e9a380e794c92dfd59`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261017_015831Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261017_015831Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `2ef66e1ba3462a071fdfa8a9f6dc134e4aaf1ab181f96a04aa0281b83324725f`
- csv_size_bytes (pre-update): `26887981`
- csv_backup_file: `brickovery_db_csv_backup_20261017_015831Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211637`
- items_db: `213474`
- items_missing_in_db: `19`
- codes_upstream: `87003`
- codes_db: `258142`
- codes_missing_in_db: `7`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261017_015831Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
