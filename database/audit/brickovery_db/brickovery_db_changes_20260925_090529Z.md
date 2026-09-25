# Brickovery DB backup & change audit — 20260925_090529Z

## Context
- created_at_utc: **20260925_090529Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3534` (id `36115824275`)
- commit: `60ac95b042134561d0bf7425a12f233feb46391a`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `252baf68c737f1a5590b31487fdf5f1062e3ae7c1ab0f68a35b595b883633c7b`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260925_090529Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260925_090529Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `a8b269ac48ab57e1a4026f95c10a9c12b4078f1e6a05b223b5256f50a950b16f`
- csv_size_bytes (pre-update): `26767302`
- csv_backup_file: `brickovery_db_csv_backup_20260925_090529Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211140`
- items_db: `212053`
- items_missing_in_db: `3`
- codes_upstream: `86708`
- codes_db: `256070`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260925_090529Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
