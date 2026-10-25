# Brickovery DB backup & change audit — 20261025_021218Z

## Context
- created_at_utc: **20261025_021218Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3804` (id `40152952684`)
- commit: `dcc38b22b93bbdaffb739ed5ca035981ae84cc34`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `29de23c06e4015d4930543761b82ecaeef5bc091df14577a59f40d960589c2fa`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261025_021218Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261025_021218Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `cfb26b149b5aa45679dd315724ec3c5f2c38196a1bf938f4490bf04dc1192a70`
- csv_size_bytes (pre-update): `26899091`
- csv_backup_file: `brickovery_db_csv_backup_20261025_021218Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211792`
- items_db: `213634`
- items_missing_in_db: `26`
- codes_upstream: `87050`
- codes_db: `258337`
- codes_missing_in_db: `18`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261025_021218Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
