# Brickovery DB backup & change audit — 20260209_052505Z

## Context
- created_at_utc: **20260209_052505Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `170` (id `21813433093`)
- commit: `8d00ef4fb5d538bbab0deb0315299a3622976c4a`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `65affd16326f7f06312ce1f4141e89d38bee46adc79785b2071c709f9dbc56e4`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260209_052505Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260209_052505Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `9ffda71a073bd1eec71c117cf9c3012393aab19f990196a3255f0485a7f511f0`
- csv_size_bytes (pre-update): `25970817`
- csv_backup_file: `brickovery_db_csv_backup_20260209_052505Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202437`
- items_db: `202430`
- items_missing_in_db: `9`
- codes_upstream: `83295`
- codes_db: `242135`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260209_052505Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
