# Brickovery DB backup & change audit — 20261002_170609Z

## Context
- created_at_utc: **20261002_170609Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3648` (id `37037533133`)
- commit: `e857718b0c60a0d29c2498e846e324c798e156ed`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `824e032a072ebb92710e988fd042e67844ea05cfc6db1e6a5f85423a37b00ff9`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261002_170609Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261002_170609Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `ab424050bdc5618838a708e0abfffc72eb552043c85c0721a22f48b361cb004c`
- csv_size_bytes (pre-update): `26858789`
- csv_backup_file: `brickovery_db_csv_backup_20261002_170609Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211400`
- items_db: `213221`
- items_missing_in_db: `15`
- codes_upstream: `86746`
- codes_db: `257642`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261002_170609Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
