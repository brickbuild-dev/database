# Brickovery DB backup & change audit — 20260520_020804Z

## Context
- created_at_utc: **20260520_020804Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2979` (id `26136715558`)
- commit: `d4a043d3cd6ff2da7da69f86b1a9e94280d077ca`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `ee168845603b8fbec7fb0fe9286053866b91bc8e2d21921b73bf3dc3ad57bd2f`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260520_020804Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260520_020804Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `74807ff939c90db84506b75fba8524d2d9c03ae3613e28fc793f90081e8a0300`
- csv_size_bytes (pre-update): `26303252`
- csv_backup_file: `brickovery_db_csv_backup_20260520_020804Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205887`
- items_db: `206373`
- items_missing_in_db: `24`
- codes_upstream: `84386`
- codes_db: `247957`
- codes_missing_in_db: `6`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260520_020804Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
