# Brickovery DB backup & change audit — 20260907_014330Z

## Context
- created_at_utc: **20260907_014330Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3351` (id `34073552198`)
- commit: `881cb5cd57e848cc221dce858dfa2d387b451371`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `852fc6e4d397659734e65961102fb282d328208652961ebf09b3091493ab8d9f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260907_014330Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260907_014330Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `7645e3968c18faacdecb0728724bae4531ba9f99b991a0eab907b48f86db738e`
- csv_size_bytes (pre-update): `26699888`
- csv_backup_file: `brickovery_db_csv_backup_20260907_014330Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210347`
- items_db: `211147`
- items_missing_in_db: `37`
- codes_upstream: `86458`
- codes_db: `254868`
- codes_missing_in_db: `26`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260907_014330Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
