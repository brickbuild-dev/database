# Brickovery DB backup & change audit — 20260921_020814Z

## Context
- created_at_utc: **20260921_020814Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3398` (id `35552889587`)
- commit: `eb9efaff16c1cf5af9c8ab7da86696f0cf562b05`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `b9f2636304a0db01c77383d28ef8905c4d342327ca263d83d4bfc98c9df764b6`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260921_020814Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260921_020814Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `61cfd81d8f171080205ca5670cd18007be7166cf143f2ba01045d1f526ca7cd3`
- csv_size_bytes (pre-update): `26748258`
- csv_backup_file: `brickovery_db_csv_backup_20260921_020814Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211063`
- items_db: `211698`
- items_missing_in_db: `234`
- codes_upstream: `86708`
- codes_db: `255708`
- codes_missing_in_db: `5`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260921_020814Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
