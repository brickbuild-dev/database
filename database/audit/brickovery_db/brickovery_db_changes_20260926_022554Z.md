# Brickovery DB backup & change audit — 20260926_022554Z

## Context
- created_at_utc: **20260926_022554Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3536` (id `36211281346`)
- commit: `952139c5739c126198ef066ee215d64b75d35473`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `35ef405bd68b275e05d475cc89f05de1cdb60e7bc589b7eb6c35cdf9f6211d67`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260926_022554Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260926_022554Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `833e1cae6877a0fca9f88662e93725e0303e290822541cdda4694c7487ce564d`
- csv_size_bytes (pre-update): `26767461`
- csv_backup_file: `brickovery_db_csv_backup_20260926_022554Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211154`
- items_db: `212056`
- items_missing_in_db: `14`
- codes_upstream: `86708`
- codes_db: `256073`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260926_022554Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
