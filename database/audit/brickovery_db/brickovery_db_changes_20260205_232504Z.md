# Brickovery DB backup & change audit — 20260205_232504Z

## Context
- created_at_utc: **20260205_232504Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `95` (id `21732405778`)
- commit: `70db70da230053965120fbee2a9b620633e11292`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `4f076871ebaadb2236ce426fc291ea49486743958028380e0e5a17e35d9128e1`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260205_232504Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260205_232504Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `ba13922c337505517a8d5239c5c5bf73d5db96655a959dcd92915e75ef1f7b15`
- csv_size_bytes (pre-update): `25487743`
- csv_backup_file: `brickovery_db_csv_backup_20260205_232504Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202403`
- items_db: `202401`
- items_missing_in_db: `2`
- codes_upstream: `83280`
- codes_db: `242094`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260205_232504Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
