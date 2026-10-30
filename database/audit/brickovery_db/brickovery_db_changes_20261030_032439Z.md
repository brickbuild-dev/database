# Brickovery DB backup & change audit — 20261030_032439Z

## Context
- created_at_utc: **20261030_032439Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3814` (id `40996368080`)
- commit: `a1ff98a9bdab8cea57da6b71670d0dac990b94f8`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `cdbc9e60b6428f5751735be62697958dc7f0c0daddeb90f2f80d00fe0830437c`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261030_032439Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261030_032439Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e82640d8ecca55bc48e8851d117b1a6bedf96efac1abb5049f3cc33f9f97c97e`
- csv_size_bytes (pre-update): `26912197`
- csv_backup_file: `brickovery_db_csv_backup_20261030_032439Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211990`
- items_db: `213805`
- items_missing_in_db: `62`
- codes_upstream: `87125`
- codes_db: `258567`
- codes_missing_in_db: `32`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261030_032439Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
