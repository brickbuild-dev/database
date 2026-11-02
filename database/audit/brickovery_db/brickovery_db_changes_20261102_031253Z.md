# Brickovery DB backup & change audit — 20261102_031253Z

## Context
- created_at_utc: **20261102_031253Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3820` (id `41380879823`)
- commit: `ab4de4e6a78057cfcc48f8e6ca542073288879fa`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `555913442dbac9ce7c731555e9c949e92a4b8e10279558b4803714f5f30c5612`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261102_031253Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261102_031253Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `6088b5253bc2de69e1e1c944598ef5c9dc4de04bc423f5c87f72f671edcd8ae3`
- csv_size_bytes (pre-update): `26918073`
- csv_backup_file: `brickovery_db_csv_backup_20261102_031253Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212024`
- items_db: `213874`
- items_missing_in_db: `28`
- codes_upstream: `87132`
- codes_db: `258669`
- codes_missing_in_db: `5`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261102_031253Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
