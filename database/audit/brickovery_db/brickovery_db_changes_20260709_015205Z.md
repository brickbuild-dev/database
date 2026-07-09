# Brickovery DB backup & change audit — 20260709_015205Z

## Context
- created_at_utc: **20260709_015205Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3118` (id `28988232698`)
- commit: `0fb12105c515e4bc3c08cfe85368beed6f67e663`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `c3be2bcfa6e2a2c380b4717eba60e1f9b748391a7fe8f93d5afd6ee68d280faf`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260709_015205Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260709_015205Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `5d2e2256f1b3d0e0be19f579556ea63fb00b9d7750c499cbd0d337fcb00a9886`
- csv_size_bytes (pre-update): `26472528`
- csv_backup_file: `brickovery_db_csv_backup_20260709_015205Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207760`
- items_db: `208431`
- items_missing_in_db: `7`
- codes_upstream: `85243`
- codes_db: `250893`
- codes_missing_in_db: `17`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260709_015205Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
