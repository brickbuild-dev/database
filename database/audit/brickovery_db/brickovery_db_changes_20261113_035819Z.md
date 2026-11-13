# Brickovery DB backup & change audit — 20261113_035819Z

## Context
- created_at_utc: **20261113_035819Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3865` (id `43361821695`)
- commit: `1913958b785962889d787557f1a4c67cf33220c1`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `054d9dec7fd9b78c128b05bb17cf0339ee612ada7e17064284dd0a0dfbecc926`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261113_035819Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261113_035819Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `7466c30067cc3066ef2ce37eaf3ea12e602ffe5c84e0abba26e4df6f3cc0235b`
- csv_size_bytes (pre-update): `26926144`
- csv_backup_file: `brickovery_db_csv_backup_20261113_035819Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212089`
- items_db: `213967`
- items_missing_in_db: `2`
- codes_upstream: `87174`
- codes_db: `258809`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261113_035819Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
