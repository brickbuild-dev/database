# Brickovery DB backup & change audit — 20260430_015305Z

## Context
- created_at_utc: **20260430_015305Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2943` (id `25143152872`)
- commit: `56908e97235c1063ae3c33415e51a5b63aa6fc4b`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `402b482060e19c40d6ddf0b46c0b8a813ec9db8df0f04c6b5400a48dfa53a186`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260430_015305Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260430_015305Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `014bd312a50b3c2c15f5f3d6416f6dbb160e1e270e86174058f90821743b545c`
- csv_size_bytes (pre-update): `26215928`
- csv_backup_file: `brickovery_db_csv_backup_20260430_015305Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205389`
- items_db: `205747`
- items_missing_in_db: `16`
- codes_upstream: `84461`
- codes_db: `246448`
- codes_missing_in_db: `134`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260430_015305Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
