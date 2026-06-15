# Brickovery DB backup & change audit — 20260615_025707Z

## Context
- created_at_utc: **20260615_025707Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3032` (id `27520841702`)
- commit: `7799d4f0d67b2846da7b294bc8955e3f3f3e1adb`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `3a504463e63866990e41b06cbe8af6f337edcb3e34f0c03ed47d246a28566217`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260615_025707Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260615_025707Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `9cc1a246e3d46d684e90cce3348953959d7cf740455f3fc9ddbd0709d7761b41`
- csv_size_bytes (pre-update): `26407638`
- csv_backup_file: `brickovery_db_csv_backup_20260615_025707Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207146`
- items_db: `207757`
- items_missing_in_db: `0`
- codes_upstream: `84790`
- codes_db: `249778`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260615_025707Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
