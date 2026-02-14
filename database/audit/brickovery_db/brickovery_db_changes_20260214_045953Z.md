# Brickovery DB backup & change audit — 20260214_045953Z

## Context
- created_at_utc: **20260214_045953Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `342` (id `22011562785`)
- commit: `1e9ca06293e628e01a43c6c4005a5ead39424011`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `72acd4c21934d5708dd79e25795e68a91944f4bd1cf8a1c840e9a1c9f199c624`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260214_045953Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260214_045953Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `08ddddcab11a276eb1dcaeb84c9593e56931e6672e0e45e896cfb3f6a0f94f0e`
- csv_size_bytes (pre-update): `25974308`
- csv_backup_file: `brickovery_db_csv_backup_20260214_045953Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202476`
- items_db: `202473`
- items_missing_in_db: `7`
- codes_upstream: `83320`
- codes_db: `242195`
- codes_missing_in_db: `5`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260214_045953Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
