# Brickovery DB backup & change audit — 20260519_020907Z

## Context
- created_at_utc: **20260519_020907Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2977` (id `26071689706`)
- commit: `92506d3897e5699123ea053f37ae34850359803a`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `5e47d5860be2db275455e134c633c24c9941e653a2c58c55f5dd0b184b0d1070`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260519_020907Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260519_020907Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `4c1720db5c994ef91361cfb1fe57d910c14c2753b3460101330adb2272f7f037`
- csv_size_bytes (pre-update): `26302062`
- csv_backup_file: `brickovery_db_csv_backup_20260519_020907Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205879`
- items_db: `206357`
- items_missing_in_db: `16`
- codes_upstream: `84378`
- codes_db: `247936`
- codes_missing_in_db: `6`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260519_020907Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
