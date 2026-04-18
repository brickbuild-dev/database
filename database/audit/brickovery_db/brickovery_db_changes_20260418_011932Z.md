# Brickovery DB backup & change audit — 20260418_011932Z

## Context
- created_at_utc: **20260418_011932Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2898` (id `24593488763`)
- commit: `4544005bce0d3083d258b4ca48105f26ef10aaae`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `e1fc86a4c8d0af42781a818643750762b159602ba2890375e24420b44ba06fc7`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260418_011932Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260418_011932Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `2971f05797d618638ae854c4c023b62628d0c3cbfffc7969d2781e6867b914bb`
- csv_size_bytes (pre-update): `26194995`
- csv_backup_file: `brickovery_db_csv_backup_20260418_011932Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205226`
- items_db: `205561`
- items_missing_in_db: `16`
- codes_upstream: `84162`
- codes_db: `246084`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260418_011932Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
