# Brickovery DB backup & change audit — 20260215_051252Z

## Context
- created_at_utc: **20260215_051252Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `344` (id `22030176146`)
- commit: `74d205c891b96c0711fa73fa7db2782b89b09b8b`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `52cbf7c88915b96696aee4ee6df74f19c5f5105a0156b1f90c95c5df30951ecf`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260215_051252Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260215_051252Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `17c524a9e77c5b21211ab94133a93eca0b437eba22d5cdf110a47bee605c3a09`
- csv_size_bytes (pre-update): `25974893`
- csv_backup_file: `brickovery_db_csv_backup_20260215_051252Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202485`
- items_db: `202480`
- items_missing_in_db: `9`
- codes_upstream: `83336`
- codes_db: `242205`
- codes_missing_in_db: `16`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260215_051252Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
