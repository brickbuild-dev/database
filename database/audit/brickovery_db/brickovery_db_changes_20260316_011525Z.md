# Brickovery DB backup & change audit — 20260316_011525Z

## Context
- created_at_utc: **20260316_011525Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `395` (id `23123853072`)
- commit: `61537e1424d34b6435d89151df898edef9ece03e`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `1e52b527efe388e9d199a7d359dbbedf4f7aa301b58e6a89362807da2d7ceac4`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260316_011525Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260316_011525Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `0a88ac49ab4935bd842697846fec6b6ebf921fffbcf3550f9c6d517bbbec41fd`
- csv_size_bytes (pre-update): `26076563`
- csv_backup_file: `brickovery_db_csv_backup_20260316_011525Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203585`
- items_db: `203633`
- items_missing_in_db: `23`
- codes_upstream: `83964`
- codes_db: `243974`
- codes_missing_in_db: `4`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260316_011525Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
