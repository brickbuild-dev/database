# Brickovery DB backup & change audit — 20261115_033915Z

## Context
- created_at_utc: **20261115_033915Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3869` (id `43672725322`)
- commit: `10ee4fb48aa2817323a63cd755ce0f0c858f6e9d`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `81a293cdd6766b75049f37704ef5e2f8cfd1be59c9c0824cdaa9c617411933a7`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261115_033915Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261115_033915Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `bc3549a69ae8b8518f16e0cc73ea75573842622168370c5125ef2c685f7f7e63`
- csv_size_bytes (pre-update): `26926657`
- csv_backup_file: `brickovery_db_csv_backup_20261115_033915Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212113`
- items_db: `213970`
- items_missing_in_db: `24`
- codes_upstream: `87181`
- codes_db: `258818`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261115_033915Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
