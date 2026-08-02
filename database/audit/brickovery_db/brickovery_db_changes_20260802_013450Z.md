# Brickovery DB backup & change audit — 20260802_013450Z

## Context
- created_at_utc: **20260802_013450Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3192` (id `30727098652`)
- commit: `1214b669e2f39d68d1c2c0ad121c6671f1d7dab4`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `e954da5cbf6be40ad5cc5f01e59310dfc6d0e82894042e1b1daab02bc5b983cf`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260802_013450Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260802_013450Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `54d02ed0ddd1da19965f8932089a2b13c7ce9e3f2c5b7ff7d1ab2b380f27d841`
- csv_size_bytes (pre-update): `26556644`
- csv_backup_file: `brickovery_db_csv_backup_20260802_013450Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209068`
- items_db: `209383`
- items_missing_in_db: `419`
- codes_upstream: `85927`
- codes_db: `252408`
- codes_missing_in_db: `134`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260802_013450Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
