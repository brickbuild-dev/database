# Brickovery DB backup & change audit — 20261019_021616Z

## Context
- created_at_utc: **20261019_021616Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3792` (id `39188546349`)
- commit: `41c30b91e4d421a5048041251980ee7b66137070`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `890d64d98f637dbd20e3122c94cf33df09fea6694c33c310773631e290ce5f8a`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261019_021616Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261019_021616Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `a4387caaab58ea246854eccdec76b5768075f470c07038a93a36dfa658889108`
- csv_size_bytes (pre-update): `26890836`
- csv_backup_file: `brickovery_db_csv_backup_20261019_021616Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211672`
- items_db: `213515`
- items_missing_in_db: `23`
- codes_upstream: `87011`
- codes_db: `258191`
- codes_missing_in_db: `6`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261019_021616Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
