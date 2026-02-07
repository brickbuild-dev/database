# Brickovery DB backup & change audit — 20260207_100339Z

## Context
- created_at_utc: **20260207_100339Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `137` (id `21778331264`)
- commit: `441b27beddda053f93bd72744d855a3043821978`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `8711aecd187e6e820032a93605fbbc536e603936edf7254c78164866cbac84b1`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260207_100339Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260207_100339Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `65273b5f98f213d3437f5ced0f1a311996d5392fcf1e22ef414905a3cc0dbe70`
- csv_size_bytes (pre-update): `25969448`
- csv_backup_file: `brickovery_db_csv_backup_20260207_100339Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202412`
- items_db: `202411`
- items_missing_in_db: `3`
- codes_upstream: `83290`
- codes_db: `242111`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260207_100339Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
