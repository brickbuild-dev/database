# Brickovery DB backup & change audit — 20260419_012852Z

## Context
- created_at_utc: **20260419_012852Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2920` (id `24618085006`)
- commit: `0b6ab8fd438fca2da4d9b0ecb5e84064bf252ac1`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `ebc44f2ce5826116442c5cc50ea8a86e0037f50717e1a42936f1b342f7c8f294`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260419_012852Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260419_012852Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `4bae95c571cd645542a85b004b77642de6e2f5cd735e9937413a435c696c0f7c`
- csv_size_bytes (pre-update): `26196059`
- csv_backup_file: `brickovery_db_csv_backup_20260419_012852Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205238`
- items_db: `205578`
- items_missing_in_db: `15`
- codes_upstream: `84162`
- codes_db: `246103`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260419_012852Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
