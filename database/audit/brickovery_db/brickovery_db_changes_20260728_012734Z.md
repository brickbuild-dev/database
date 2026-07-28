# Brickovery DB backup & change audit — 20260728_012734Z

## Context
- created_at_utc: **20260728_012734Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3182` (id `30319975296`)
- commit: `14184109307e6f87d354f952a69f4fcca6f44a6a`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `75dfbbcbb95d7851896ff25d62bbdf0b8bb8fa1dfec1193513617681e40f3ca3`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260728_012734Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260728_012734Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `96406e1bff92968594e70470d6baa8c4df93974e31d297742c695d3b15977589`
- csv_size_bytes (pre-update): `26505428`
- csv_backup_file: `brickovery_db_csv_backup_20260728_012734Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `208121`
- items_db: `208830`
- items_missing_in_db: `17`
- codes_upstream: `85417`
- codes_db: `251477`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260728_012734Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
