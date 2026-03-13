# Brickovery DB backup & change audit — 20260313_011235Z

## Context
- created_at_utc: **20260313_011235Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `389` (id `23031387435`)
- commit: `e955a285516ac229313fb1979c162a12d62d094d`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `76d67b6f556a436fb4e12e5647bd33548c705f6c8fa354849552b83cae0f96ee`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260313_011235Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260313_011235Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `d967676fbd3c05845ea637877b2707212fa86b20754d95d02e1939c87e5eaff6`
- csv_size_bytes (pre-update): `26069591`
- csv_backup_file: `brickovery_db_csv_backup_20260313_011235Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203485`
- items_db: `203534`
- items_missing_in_db: `19`
- codes_upstream: `83941`
- codes_db: `243853`
- codes_missing_in_db: `3`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260313_011235Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
