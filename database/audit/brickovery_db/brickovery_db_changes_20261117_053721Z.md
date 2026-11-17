# Brickovery DB backup & change audit — 20261117_053721Z

## Context
- created_at_utc: **20261117_053721Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3873` (id `44024501792`)
- commit: `1604453edbdd04cda5bd9570114280f0e0a06340`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `977e178e57c03a70c984a8d227aef2f8336252608bac4460d4879de1ae9fccf3`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261117_053721Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261117_053721Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `4796d1444e43957d3db61a1a3c489c4e22e4c7b6461293cc7f9c29bcb2e5d93c`
- csv_size_bytes (pre-update): `26928874`
- csv_backup_file: `brickovery_db_csv_backup_20261117_053721Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212144`
- items_db: `214006`
- items_missing_in_db: `20`
- codes_upstream: `87183`
- codes_db: `258856`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261117_053721Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
