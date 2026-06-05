# Brickovery DB backup & change audit — 20260605_021251Z

## Context
- created_at_utc: **20260605_021251Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3011` (id `26991001356`)
- commit: `c205733c75857d214eeff7d969a1b3eb07d25159`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `d922f01230c7e63db1d0c42f3d7261049412f2b7653c85f1f8850c71a778a407`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260605_021251Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260605_021251Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `80b56b9b3f999a121dd6d493869eb8ead721fa8d0d9f6a66c76580859d270453`
- csv_size_bytes (pre-update): `26354140`
- csv_backup_file: `brickovery_db_csv_backup_20260605_021251Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206557`
- items_db: `207120`
- items_missing_in_db: `28`
- codes_upstream: `84470`
- codes_db: `248832`
- codes_missing_in_db: `15`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260605_021251Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
