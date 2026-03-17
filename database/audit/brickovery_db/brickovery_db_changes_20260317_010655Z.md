# Brickovery DB backup & change audit — 20260317_010655Z

## Context
- created_at_utc: **20260317_010655Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `397` (id `23173501620`)
- commit: `a1f7d9eb1aa3f4e2ac5a2b57995df513faff0ef3`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `710d8c98dcf4cc2cfff1e933198f17aa483c0cdfba2e4e346cc8b9bbbddfab01`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260317_010655Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260317_010655Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `89b203f756ad7da2cd882218dcc34c8b325aa3ee025995c28a12df67235e3867`
- csv_size_bytes (pre-update): `26078073`
- csv_backup_file: `brickovery_db_csv_backup_20260317_010655Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203630`
- items_db: `203656`
- items_missing_in_db: `48`
- codes_upstream: `83995`
- codes_db: `244001`
- codes_missing_in_db: `29`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260317_010655Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
