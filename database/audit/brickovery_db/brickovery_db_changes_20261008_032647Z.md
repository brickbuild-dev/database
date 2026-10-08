# Brickovery DB backup & change audit — 20261008_032647Z

## Context
- created_at_utc: **20261008_032647Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3660` (id `37722112566`)
- commit: `a90d0140daf93e14303f0faafb1dc474acb9d1a1`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `8280bd6fd44552d0b0c11313f9a5c066b1b600cd6df5af313c3a15ad470c2180`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261008_032647Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261008_032647Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8355bf0ab71a04da6adc2a640939b46cff7902f873f7e1faaf7c9cfe89344f23`
- csv_size_bytes (pre-update): `26873968`
- csv_backup_file: `brickovery_db_csv_backup_20261008_032647Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211530`
- items_db: `213351`
- items_missing_in_db: `21`
- codes_upstream: `86906`
- codes_db: `257903`
- codes_missing_in_db: `21`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261008_032647Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
