# Brickovery DB backup & change audit — 20260725_013239Z

## Context
- created_at_utc: **20260725_013239Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3176` (id `30138463472`)
- commit: `3c3599bde5a3d1aaec424a3ca9fe47a9af8d187a`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `f0c6ee4aee1b1b3b3cdec9a322095d4e3631a410e45c5793264e3bccfa64a2b3`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260725_013239Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260725_013239Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e5ec94b06c2e300e3aad7157f9d5a4dcbe4b97ec27cb85b9ac4ae82eabbef53b`
- csv_size_bytes (pre-update): `26501460`
- csv_backup_file: `brickovery_db_csv_backup_20260725_013239Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `208058`
- items_db: `208761`
- items_missing_in_db: `1`
- codes_upstream: `85406`
- codes_db: `251400`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260725_013239Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
