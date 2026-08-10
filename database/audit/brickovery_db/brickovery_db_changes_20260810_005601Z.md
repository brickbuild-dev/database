# Brickovery DB backup & change audit — 20260810_005601Z

## Context
- created_at_utc: **20260810_005601Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3208` (id `31345432902`)
- commit: `30a1756b3cdb8eb7ebaa26f02c31bb2e1d76799c`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `381d201d269235301e1a158b177ac1ff001add15b347c747e3ede5a944f6d7f1`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260810_005601Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260810_005601Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `31d7949e281b946919f1de6891c2665ee2446eeced18923bb8c248494fda6752`
- csv_size_bytes (pre-update): `26612658`
- csv_backup_file: `brickovery_db_csv_backup_20260810_005601Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209409`
- items_db: `210103`
- items_missing_in_db: `81`
- codes_upstream: `86019`
- codes_db: `253375`
- codes_missing_in_db: `4`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260810_005601Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
