# Brickovery DB backup & change audit — 20260609_020018Z

## Context
- created_at_utc: **20260609_020018Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3019` (id `27178873251`)
- commit: `4aca775a6288f43b9448ba225586697f4093a3ed`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `dcd058f0869a6548f744661382e93ad58654985267f85350893768f1b9da8a27`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260609_020018Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260609_020018Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e5c92a4a5d391fb0a76da6e7d924de6f52ba179981c83dd783b6a7fe97e4d3e2`
- csv_size_bytes (pre-update): `26366801`
- csv_backup_file: `brickovery_db_csv_backup_20260609_020018Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206671`
- items_db: `207232`
- items_missing_in_db: `36`
- codes_upstream: `84592`
- codes_db: `249051`
- codes_missing_in_db: `23`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260609_020018Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
