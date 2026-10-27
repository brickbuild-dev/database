# Brickovery DB backup & change audit — 20261027_024742Z

## Context
- created_at_utc: **20261027_024742Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3808` (id `40439861276`)
- commit: `e6ef4600e16129a38b22fdc794a61ceaf6543588`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `28e81c1357172172d305f7b0d10b095c7b8ec5a626cc10e41a181f40596ba619`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261027_024742Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261027_024742Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `45b78fea2e82527b318a837cfb7fe6bed206b713ba0d0c64610c95ebc76a5bea`
- csv_size_bytes (pre-update): `26904538`
- csv_backup_file: `brickovery_db_csv_backup_20261027_024742Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211837`
- items_db: `213696`
- items_missing_in_db: `13`
- codes_upstream: `87068`
- codes_db: `258431`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261027_024742Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
