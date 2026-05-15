# Brickovery DB backup & change audit — 20260515_020230Z

## Context
- created_at_utc: **20260515_020230Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2969` (id `25896061494`)
- commit: `4bd5eb5f255249ec8db05bd53d05eacc15e1d797`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `fff90a28e873a859c060f59656288ffb7201fd8895c436bc5337ba63832c928e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260515_020230Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260515_020230Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `079e0ef546264827293f805c8f2b260fd15cb870dd1c7b3c90dbde81f4ffa462`
- csv_size_bytes (pre-update): `26284762`
- csv_backup_file: `brickovery_db_csv_backup_20260515_020230Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205845`
- items_db: `206187`
- items_missing_in_db: `128`
- codes_upstream: `84366`
- codes_db: `247636`
- codes_missing_in_db: `133`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260515_020230Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
