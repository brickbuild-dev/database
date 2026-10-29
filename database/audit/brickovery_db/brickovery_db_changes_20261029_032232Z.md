# Brickovery DB backup & change audit — 20261029_032232Z

## Context
- created_at_utc: **20261029_032232Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3812` (id `40810868515`)
- commit: `f5b8060d9c29855cee7fe0612736c04b99d82086`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `e943f64063abe3cd0babaca73c10b1266375945603f7731573fdda2c78e15dfd`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261029_032232Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261029_032232Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e31496253c9c17f3a941650808fa707943a14eb953375999a25635228d4e7387`
- csv_size_bytes (pre-update): `26906771`
- csv_backup_file: `brickovery_db_csv_backup_20261029_032232Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211928`
- items_db: `213732`
- items_missing_in_db: `73`
- codes_upstream: `87093`
- codes_db: `258471`
- codes_missing_in_db: `23`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261029_032232Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
