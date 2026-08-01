# Brickovery DB backup & change audit — 20260801_015009Z

## Context
- created_at_utc: **20260801_015009Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3190` (id `30678501588`)
- commit: `70c39a68ee5867762531bafe92ef96576a6cd4dc`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `5d64e2456fa8cbdcb290a7bc2a4978418df5db5aef27d0cfd04f16cbc7980848`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260801_015009Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260801_015009Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `5601e9d5372cff92191a5713e47ea23a07531b2c4f05ac63fd1880df738878c8`
- csv_size_bytes (pre-update): `26533529`
- csv_backup_file: `brickovery_db_csv_backup_20260801_015009Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `208649`
- items_db: `208997`
- items_missing_in_db: `386`
- codes_upstream: `85793`
- codes_db: `251972`
- codes_missing_in_db: `52`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260801_015009Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
