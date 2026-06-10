# Brickovery DB backup & change audit — 20260610_021240Z

## Context
- created_at_utc: **20260610_021240Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3021` (id `27248297939`)
- commit: `75cfa4db4c880909542a1478e42ec4465f59b348`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `3a02b748ae519ac8dfde5dbf0a384998997d4d2d92c33e3a07001bf0e197932e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260610_021240Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260610_021240Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8958eb6b6e3f14110227f17705a22fe1c3f7c60c972f56f1e82978f1087d646a`
- csv_size_bytes (pre-update): `26369791`
- csv_backup_file: `brickovery_db_csv_backup_20260610_021240Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206688`
- items_db: `207268`
- items_missing_in_db: `17`
- codes_upstream: `84638`
- codes_db: `249105`
- codes_missing_in_db: `45`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260610_021240Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
