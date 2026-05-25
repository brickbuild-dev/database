# Brickovery DB backup & change audit — 20260525_021350Z

## Context
- created_at_utc: **20260525_021350Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2989` (id `26379532412`)
- commit: `aa1cac50200afc0c6edb9374a8425e7a483c6a92`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `c4073cc0f2d52bb537a1c4f30ec47dae9856f7bed7c84bf0138e4a1f9ed46fa2`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260525_021350Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260525_021350Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `c504f4435d986c8a915739de7e985ea972b0132c6d32229eb155e77dc6dd62bd`
- csv_size_bytes (pre-update): `26314346`
- csv_backup_file: `brickovery_db_csv_backup_20260525_021350Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205931`
- items_db: `206480`
- items_missing_in_db: `13`
- codes_upstream: `84409`
- codes_db: `248153`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260525_021350Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
