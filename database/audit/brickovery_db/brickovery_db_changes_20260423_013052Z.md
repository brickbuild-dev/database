# Brickovery DB backup & change audit — 20260423_013052Z

## Context
- created_at_utc: **20260423_013052Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2928` (id `24811523909`)
- commit: `e1a1aee7eb3f14a2e13a864b83666effe8012090`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `8609335c9c62a959cfffdf8b9306edbcdefa18edae2ddc07b1b78827340a8f2f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260423_013052Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260423_013052Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `f78a6547cf0d0bd03c74f4bbea33cafea5f42b4d6bd722f5f55998928d5a68b7`
- csv_size_bytes (pre-update): `26201126`
- csv_backup_file: `brickovery_db_csv_backup_20260423_013052Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205279`
- items_db: `205644`
- items_missing_in_db: `2`
- codes_upstream: `84171`
- codes_db: `246192`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260423_013052Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
