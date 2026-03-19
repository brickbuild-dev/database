# Brickovery DB backup & change audit — 20260319_011009Z

## Context
- created_at_utc: **20260319_011009Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `401` (id `23274875561`)
- commit: `0338b4ca2c719b474d1fb37dc6a989ad31366eac`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `6b900a42d45c376bc8687123a6d309fdd2241b5a43e1d43aba40a5061de61155`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260319_011009Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260319_011009Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d900cb0345ac669a2cc09233e253e1729a4cc70349bbf9b8af2a15d9f0736b44`
- csv_size_bytes (pre-update): `26085822`
- csv_backup_file: `brickovery_db_csv_backup_20260319_011009Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203693`
- items_db: `203746`
- items_missing_in_db: `22`
- codes_upstream: `84011`
- codes_db: `244135`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260319_011009Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
