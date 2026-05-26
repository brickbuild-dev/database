# Brickovery DB backup & change audit — 20260526_020425Z

## Context
- created_at_utc: **20260526_020425Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2991` (id `26427954528`)
- commit: `3443b1584ed7dba62ec37587c2b7e5c1374182a2`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `2e712639e80d836c1dcb8b3c106eea40e69a09cb5b679315a9ef023f561c8f07`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260526_020425Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260526_020425Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `be194f2cc8e14122cdb3b429b00b7b4b7901823037db5edc13dc322f4981098f`
- csv_size_bytes (pre-update): `26315138`
- csv_backup_file: `brickovery_db_csv_backup_20260526_020425Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205935`
- items_db: `206493`
- items_missing_in_db: `7`
- codes_upstream: `84409`
- codes_db: `248166`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260526_020425Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
