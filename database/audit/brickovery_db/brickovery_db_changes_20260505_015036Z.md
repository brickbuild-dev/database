# Brickovery DB backup & change audit — 20260505_015036Z

## Context
- created_at_utc: **20260505_015036Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2953` (id `25353430181`)
- commit: `ce5f783ee10099ce74b27ecde1add1e35b7665c6`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `69c9e967e39b0dfab443b4c7f4ca2bfabb4294bb3239b9d9e8bfd5fd58e9fea5`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260505_015036Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260505_015036Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `0806ecf08a851018697fbf45bcaea78265473eed21f4f8659bb07d7fb6167d18`
- csv_size_bytes (pre-update): `26257390`
- csv_backup_file: `brickovery_db_csv_backup_20260505_015036Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205657`
- items_db: `206048`
- items_missing_in_db: `9`
- codes_upstream: `84853`
- codes_db: `247164`
- codes_missing_in_db: `121`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260505_015036Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
