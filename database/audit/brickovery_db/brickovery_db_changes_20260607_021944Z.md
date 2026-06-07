# Brickovery DB backup & change audit — 20260607_021944Z

## Context
- created_at_utc: **20260607_021944Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3015` (id `27080086249`)
- commit: `c65d077d7d5114ffdd26609593f4aa0c9e25d819`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `8fe095e36bcf0ecf61204ef86ea77119b00f2695d14e170b8e93dae4fc7118bb`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260607_021944Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260607_021944Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `93df71f2e18a54d57b2dd3e8d27baedebccf8cfaf1c706526828578576a1c8f3`
- csv_size_bytes (pre-update): `26357516`
- csv_backup_file: `brickovery_db_csv_backup_20260607_021944Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206609`
- items_db: `207157`
- items_missing_in_db: `46`
- codes_upstream: `84523`
- codes_db: `248890`
- codes_missing_in_db: `44`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260607_021944Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
