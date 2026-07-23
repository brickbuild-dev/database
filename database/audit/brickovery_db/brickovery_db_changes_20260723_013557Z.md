# Brickovery DB backup & change audit — 20260723_013557Z

## Context
- created_at_utc: **20260723_013557Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3172` (id `29971913249`)
- commit: `d81866614ee34edff323b5fc27779e22570a6ca1`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `2513770f8c9ab3df466445ab30144bc20432655abe0e4c1e6c9d3710f92baec3`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260723_013557Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260723_013557Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `b7f85f139479476f8c231df051c371f4eeb5e8f75de38c77a7d31a053b5b5cf8`
- csv_size_bytes (pre-update): `26500334`
- csv_backup_file: `brickovery_db_csv_backup_20260723_013557Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `208047`
- items_db: `208741`
- items_missing_in_db: `10`
- codes_upstream: `85405`
- codes_db: `251380`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260723_013557Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
