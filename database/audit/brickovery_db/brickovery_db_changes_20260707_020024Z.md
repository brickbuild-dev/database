# Brickovery DB backup & change audit — 20260707_020024Z

## Context
- created_at_utc: **20260707_020024Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3114` (id `28835922408`)
- commit: `5c7c8075071f09eda95c9290d14fe1336ebd3644`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `83e5f3e889d9d7e6c70f1c6a7e8c74cdd97fde81793d07095b10360169dfab1c`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260707_020024Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260707_020024Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `94c808b3939e33a1a106e55aea78b34c9868ceba6a16d8b9c3207cbe8fe3384b`
- csv_size_bytes (pre-update): `26471082`
- csv_backup_file: `brickovery_db_csv_backup_20260707_020024Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207740`
- items_db: `208415`
- items_missing_in_db: `3`
- codes_upstream: `85214`
- codes_db: `250868`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260707_020024Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
