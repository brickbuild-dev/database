# Brickovery DB backup & change audit — 20260805_012936Z

## Context
- created_at_utc: **20260805_012936Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3198` (id `30966177052`)
- commit: `ef5c23b941e18fee40adaedd9e73c202d081edbc`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `c37b4619e2c89dc522ca3f13b85fb86060f287f19bb4bbb516b163c79d3219fe`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260805_012936Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260805_012936Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `dea86bbfaa4ae8bf6c52ec97ba6c6c5f5e507226d4dfd838d445d85aa4d59d75`
- csv_size_bytes (pre-update): `26596022`
- csv_backup_file: `brickovery_db_csv_backup_20260805_012936Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209117`
- items_db: `209861`
- items_missing_in_db: `29`
- codes_upstream: `86010`
- codes_db: `253079`
- codes_missing_in_db: `20`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260805_012936Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
