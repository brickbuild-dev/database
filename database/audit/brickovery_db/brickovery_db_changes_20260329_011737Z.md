# Brickovery DB backup & change audit — 20260329_011737Z

## Context
- created_at_utc: **20260329_011737Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `437` (id `23698422914`)
- commit: `c0934163be73491c2e6e39970f3bb7aa462ce1ee`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `e1ef38e93cae35428f5cc86ac8fec9af2a2b6455e89d2d3622dce2258a0b5e82`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260329_011737Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260329_011737Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `04e8d68cb6daec027f66cadecfa569ea7df20d8aab746782aa3afa92d7cc7273`
- csv_size_bytes (pre-update): `26136535`
- csv_backup_file: `brickovery_db_csv_backup_20260329_011737Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `204540`
- items_db: `204631`
- items_missing_in_db: `228`
- codes_upstream: `84066`
- codes_db: `245071`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260329_011737Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
