# Brickovery DB backup & change audit — 20260207_110521Z

## Context
- created_at_utc: **20260207_110521Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `138` (id `21779065397`)
- commit: `8c0aaf0d1d20757a942c33e51fe563edc38c1272`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `d7ec1ce52fd15db31afcc891c76ef5908113bb3ece27740e5c85ea96dd92143c`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260207_110521Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260207_110521Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `bb1360415428dd116d31abf9fde255b163bcbc2178b9344b2e7948bc1564b6c6`
- csv_size_bytes (pre-update): `25969602`
- csv_backup_file: `brickovery_db_csv_backup_20260207_110521Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202414`
- items_db: `202414`
- items_missing_in_db: `2`
- codes_upstream: `83290`
- codes_db: `242114`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260207_110521Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
