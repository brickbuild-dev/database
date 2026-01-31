# Brickovery DB backup & change audit — 20260131_045116Z

## Context
- created_at_utc: **20260131_045116Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync upstream + update brickovery DB (semantic + chunked rebuild)`
- run: `43` (id `21539031815`)
- commit: `455f7bcc9c141a7c8d20df93599289ad851aa47e`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `dce15a77cc8e4c19985ab2bd98a6769eef79cefc7b87526997d5a3813b41f001`
- db_size_bytes (pre-update): `44457984`
- backup_file: `brickovery_db_backup_20260131_045116Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260131_045116Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `a2ffa5fce18b97fbbf63b21115d4424fc916e098ce60bc7780286968d809393b`
- csv_size_bytes (pre-update): `16157592`
- csv_backup_file: `brickovery_db_csv_backup_20260131_045116Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202334`
- items_db: `237871`
- items_missing_in_db: `3`
- codes_upstream: `83271`
- codes_db: `282484`
- codes_missing_in_db: `17`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260131_045116Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
