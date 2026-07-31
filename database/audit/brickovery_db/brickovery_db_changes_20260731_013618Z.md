# Brickovery DB backup & change audit — 20260731_013618Z

## Context
- created_at_utc: **20260731_013618Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3188` (id `30596455774`)
- commit: `a15b8b8abb056c2c6fe0dc33c33a7ed659b36d69`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `d3d36f41cc0b618062010787e33d311e2471b51a212ae2b8c489701a316661fc`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260731_013618Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260731_013618Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `da1ba8fec0472cb4dce902d7fdd3bd282d11a83c2e7d0b5ea867a40b8ffb7998`
- csv_size_bytes (pre-update): `26510229`
- csv_backup_file: `brickovery_db_csv_backup_20260731_013618Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `208269`
- items_db: `208913`
- items_missing_in_db: `84`
- codes_upstream: `85745`
- codes_db: `251563`
- codes_missing_in_db: `325`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260731_013618Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
