# Brickovery DB backup & change audit — 20260619_025302Z

## Context
- created_at_utc: **20260619_025302Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3068` (id `27802236679`)
- commit: `4b2664f63a7935aa4d45b431998f8648dda327a4`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `55edc45be8a3daf8f92f054e4497801d33867466066d75a3a92a129ac1b6cdde`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260619_025302Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260619_025302Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e8bc234cbccdc28832720ea19ff9a5b4c526dffc4c13f2800193973d1277a959`
- csv_size_bytes (pre-update): `26420659`
- csv_backup_file: `brickovery_db_csv_backup_20260619_025302Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207265`
- items_db: `207883`
- items_missing_in_db: `13`
- codes_upstream: `84899`
- codes_db: `250002`
- codes_missing_in_db: `4`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260619_025302Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
