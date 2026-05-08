# Brickovery DB backup & change audit — 20260508_015836Z

## Context
- created_at_utc: **20260508_015836Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2959` (id `25532137751`)
- commit: `6bbe1b69095d7608d1d56007e4878190c7944e29`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `7bcc1358c5ff5c6b45bfdd3c9902d4de5d3d785ff90c862eefaa2fe1d52cf07a`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260508_015836Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260508_015836Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `ca48c826c4f25c5804bc17962c42810c96eb21e196503572d5401bb22d8748e4`
- csv_size_bytes (pre-update): `26277592`
- csv_backup_file: `brickovery_db_csv_backup_20260508_015836Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205700`
- items_db: `206127`
- items_missing_in_db: `10`
- codes_upstream: `84765`
- codes_db: `247513`
- codes_missing_in_db: `20`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260508_015836Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
