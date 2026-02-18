# Brickovery DB backup & change audit — 20260218_051644Z

## Context
- created_at_utc: **20260218_051644Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `350` (id `22127569140`)
- commit: `da3a8c62988a517db23fe24c40f35b12ce604645`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `7ff69e3fad81210d2fd4449995c7bd2c99aedb89d10c35cb5250ff9422520b52`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260218_051644Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260218_051644Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `ef0a168aa91d658b95dd0650a243aba6f5d2b6d5eb8b3e925d106ab41fb0a5e2`
- csv_size_bytes (pre-update): `25984060`
- csv_backup_file: `brickovery_db_csv_backup_20260218_051644Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202524`
- items_db: `202529`
- items_missing_in_db: `2`
- codes_upstream: `83441`
- codes_db: `242364`
- codes_missing_in_db: `11`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260218_051644Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
