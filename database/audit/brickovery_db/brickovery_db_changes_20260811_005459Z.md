# Brickovery DB backup & change audit — 20260811_005459Z

## Context
- created_at_utc: **20260811_005459Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3210` (id `31447243592`)
- commit: `4d6d4487035462e5107d6b4a5e302017cbf30bbc`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `1ac512599ada903688a6c6d2d9d34f9ee8619d34862272f4b35727faa910a89d`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260811_005459Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260811_005459Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `329d0482637b255a2fcae3f1b01398b1ae3f68dd510cf0e9ce9f4bb267cab548`
- csv_size_bytes (pre-update): `26617465`
- csv_backup_file: `brickovery_db_csv_backup_20260811_005459Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `209448`
- items_db: `210184`
- items_missing_in_db: `39`
- codes_upstream: `86048`
- codes_db: `253460`
- codes_missing_in_db: `30`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `1`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260811_005459Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
