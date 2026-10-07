# Brickovery DB backup & change audit — 20261007_030821Z

## Context
- created_at_utc: **20261007_030821Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3658` (id `37564846282`)
- commit: `97c48fb7f7050577de201132dd9daff0c9f527e6`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `a97e73265ba75942a792fbff9c0ae2c287217209967402569c962e4f7e046531`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261007_030821Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261007_030821Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `36a8d9f84d98e41d7bbbbae8b7c59c168ef76ae3f581813c1335b826cc28d398`
- csv_size_bytes (pre-update): `26871299`
- csv_backup_file: `brickovery_db_csv_backup_20261007_030821Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211509`
- items_db: `213329`
- items_missing_in_db: `22`
- codes_upstream: `86885`
- codes_db: `257857`
- codes_missing_in_db: `26`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261007_030821Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
