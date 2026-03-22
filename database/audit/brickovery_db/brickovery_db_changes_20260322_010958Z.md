# Brickovery DB backup & change audit — 20260322_010958Z

## Context
- created_at_utc: **20260322_010958Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `407` (id `23392723903`)
- commit: `0a94bd22cbcc9f7ec5b25a0d7ad1b8d5b24815ac`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `a1e960eed833f0dd30bd3d4e3232f19e57f33fd8cc73dba04df11c2ca3c409e9`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260322_010958Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260322_010958Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `af27518fd94531498c2bb91f33b27ad867328e681f0e7a4cfb0c1df3eb972547`
- csv_size_bytes (pre-update): `26090248`
- csv_backup_file: `brickovery_db_csv_backup_20260322_010958Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203724`
- items_db: `203798`
- items_missing_in_db: `11`
- codes_upstream: `84052`
- codes_db: `244213`
- codes_missing_in_db: `9`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260322_010958Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
