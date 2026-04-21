# Brickovery DB backup & change audit — 20260421_012616Z

## Context
- created_at_utc: **20260421_012616Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2924` (id `24699038854`)
- commit: `04e726043bfdb82c5a4ebad85dd2206bdfdf1c25`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `af44770ed4a55fcc72770c8d9d610f53ce8bfe42639fd4c9ea2f3c455df6a0f8`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260421_012616Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260421_012616Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d571ba6c0219a151c94f0fe679e1397f316c35fbabb1e5cc7d0241b05c5067dc`
- csv_size_bytes (pre-update): `26198697`
- csv_backup_file: `brickovery_db_csv_backup_20260421_012616Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205257`
- items_db: `205615`
- items_missing_in_db: `5`
- codes_upstream: `84171`
- codes_db: `246148`
- codes_missing_in_db: `16`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260421_012616Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
