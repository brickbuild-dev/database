# Brickovery DB backup & change audit — 20260611_023742Z

## Context
- created_at_utc: **20260611_023742Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3023` (id `27319799760`)
- commit: `72ab7837fee61092b75086586eee86eff67885fb`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `f7b0cab98a9dd7d8aa085435a0d312f50b568cfa209d2e2348af666f178306e8`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260611_023742Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260611_023742Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `f27141dda6f76f915ecbc41177bc4abcf506649f84adef34bf24f4a0c471341d`
- csv_size_bytes (pre-update): `26373341`
- csv_backup_file: `brickovery_db_csv_backup_20260611_023742Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206710`
- items_db: `207285`
- items_missing_in_db: `24`
- codes_upstream: `84665`
- codes_db: `249167`
- codes_missing_in_db: `26`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260611_023742Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
