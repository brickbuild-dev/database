# Brickovery DB backup & change audit — 20260628_021420Z

## Context
- created_at_utc: **20260628_021420Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3097` (id `28308481884`)
- commit: `1354a8230f89f57f11211bce4e47919902575c06`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `b746b120675e2c61eb8589e1c51625f8a28bc68537352171ecee42bb05da4c6f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260628_021420Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260628_021420Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `bca5bdd2ac3dbbbab3c61c6277e8ba938ade20238d037664803a06f742a5ddc8`
- csv_size_bytes (pre-update): `26449826`
- csv_backup_file: `brickovery_db_csv_backup_20260628_021420Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207535`
- items_db: `208203`
- items_missing_in_db: `4`
- codes_upstream: `85062`
- codes_db: `250502`
- codes_missing_in_db: `4`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260628_021420Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
