# Brickovery DB backup & change audit — 20260503_015004Z

## Context
- created_at_utc: **20260503_015004Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2949` (id `25266973292`)
- commit: `7b27415593e381e3f787eccece04f77a066887a8`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `7b75d40e4c52641c193a0814da37cfdd2c6495c2004b05ca4e1c1264d215b736`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260503_015004Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260503_015004Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8267397c046e1305b80d5f023ae3b9ac019248a806bfb2c5851135cdcf9a60b3`
- csv_size_bytes (pre-update): `26236080`
- csv_backup_file: `brickovery_db_csv_backup_20260503_015004Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205583`
- items_db: `205906`
- items_missing_in_db: `73`
- codes_upstream: `84673`
- codes_db: `246795`
- codes_missing_in_db: `170`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260503_015004Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
