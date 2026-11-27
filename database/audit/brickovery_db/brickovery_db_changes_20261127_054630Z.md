# Brickovery DB backup & change audit — 20261127_054630Z

## Context
- created_at_utc: **20261127_054630Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3896` (id `45947112155`)
- commit: `644a9d1822ec528a1922807ac4f8678a4b804b63`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `2ee4984140cc3a75d94f2197c6f39a2edcf7e9dcf30eaad18cd6c257748c5991`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261127_054630Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261127_054630Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `603f246e38c588d747e0574e7f73e8028d0f7ab77c95389b634abe210ce5bfd4`
- csv_size_bytes (pre-update): `26933814`
- csv_backup_file: `brickovery_db_csv_backup_20261127_054630Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212208`
- items_db: `214077`
- items_missing_in_db: `17`
- codes_upstream: `87201`
- codes_db: `258941`
- codes_missing_in_db: `3`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261127_054630Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
