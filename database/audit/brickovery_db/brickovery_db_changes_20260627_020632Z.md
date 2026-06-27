# Brickovery DB backup & change audit — 20260627_020632Z

## Context
- created_at_utc: **20260627_020632Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3095` (id `28275192425`)
- commit: `620db18a3b56a7c0dd3257cc42509e76bd2ad510`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `9e28b3f56c018fbb7f78c287504a569b1c6a6cd0a5596627df75007e8d25e545`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260627_020632Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260627_020632Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `cc32fa97df5c489e12b3355edc8372b9b036a72b1f5c6e3df0d6465e383ba41a`
- csv_size_bytes (pre-update): `26446770`
- csv_backup_file: `brickovery_db_csv_backup_20260627_020632Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207532`
- items_db: `208182`
- items_missing_in_db: `21`
- codes_upstream: `85058`
- codes_db: `250450`
- codes_missing_in_db: `31`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260627_020632Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
