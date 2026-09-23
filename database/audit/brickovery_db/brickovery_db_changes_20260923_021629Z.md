# Brickovery DB backup & change audit — 20260923_021629Z

## Context
- created_at_utc: **20260923_021629Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3402` (id `35809218884`)
- commit: `f3bcc3034cce4dd604c7d63105502658e9a6544f`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `5194eede19a2f151c6bf1233a13f45ca97356c02af8242a0a7f5e783762edb0f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260923_021629Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260923_021629Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `0580c4f95ea9d04563a3dc6195f37a9da3f5dbc7088ea2c44cc27bc0edebfd09`
- csv_size_bytes (pre-update): `26762287`
- csv_backup_file: `brickovery_db_csv_backup_20260923_021629Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211105`
- items_db: `211956`
- items_missing_in_db: `39`
- codes_upstream: `86710`
- codes_db: `255972`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260923_021629Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
