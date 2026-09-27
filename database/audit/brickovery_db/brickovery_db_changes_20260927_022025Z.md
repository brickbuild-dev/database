# Brickovery DB backup & change audit — 20260927_022025Z

## Context
- created_at_utc: **20260927_022025Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3538` (id `36287876678`)
- commit: `11f496e0ca146db899e9af85194bd97fe06ebbbc`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `0fcb4035ca46ab811500f2aa36c14ee8c87814ae81eca322784cb0cc5f90576a`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260927_022025Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260927_022025Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8aad07ba531f2f04b31f0560a473771c8ded51d8a60e1e0604e118a4d14fbef7`
- csv_size_bytes (pre-update): `26768228`
- csv_backup_file: `brickovery_db_csv_backup_20260927_022025Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211161`
- items_db: `212070`
- items_missing_in_db: `7`
- codes_upstream: `86710`
- codes_db: `256087`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260927_022025Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
