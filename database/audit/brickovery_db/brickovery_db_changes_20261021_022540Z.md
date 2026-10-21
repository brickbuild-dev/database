# Brickovery DB backup & change audit — 20261021_022540Z

## Context
- created_at_utc: **20261021_022540Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3796` (id `39532203522`)
- commit: `0f81d793f5b218991434f32fa39c82f34399bdce`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `f8cff9dae7cdaa102889a9e890117b91ab0ae8e8bd1035b95c23a7206deb9ca4`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261021_022540Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261021_022540Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `1d23f66fe74c9ebc8c4feb22bc293abae118c77e36778d2c8cad0472964d6460`
- csv_size_bytes (pre-update): `26893617`
- csv_backup_file: `brickovery_db_csv_backup_20261021_022540Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211706`
- items_db: `213554`
- items_missing_in_db: `19`
- codes_upstream: `87018`
- codes_db: `258240`
- codes_missing_in_db: `3`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261021_022540Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
