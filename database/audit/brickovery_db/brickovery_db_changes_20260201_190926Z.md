# Brickovery DB backup & change audit — 20260201_190926Z

## Context
- created_at_utc: **20260201_190926Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `71` (id `21568567231`)
- commit: `3b84e6734d2981e194c046feb86abce8baa7da7d`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `7b20b49edf2a69995c282d5afdbcdc256096dc5d5188712e425fc8ab656405b6`
- db_size_bytes (pre-update): `44695552`
- backup_file: `brickovery_db_backup_20260201_190926Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260201_190926Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e519823982e9812a2da4f913935a101697269d6e3ccd2e8319b44cfaea3568d6`
- csv_size_bytes (pre-update): `16155986`
- csv_backup_file: `brickovery_db_csv_backup_20260201_190926Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202369`
- items_db: `237874`
- items_missing_in_db: `35`
- codes_upstream: `83273`
- codes_db: `282504`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260201_190926Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
