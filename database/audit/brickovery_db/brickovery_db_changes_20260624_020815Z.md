# Brickovery DB backup & change audit — 20260624_020815Z

## Context
- created_at_utc: **20260624_020815Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3089` (id `28070015924`)
- commit: `294082b488f23591a2c3733659bc276a8595abc7`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `cdcdab4a5ba9d6da0944f84b7bf66823c4d46362b269585dc91f6774edf3a4d6`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260624_020815Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260624_020815Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `79810f6f47bedaf6e1e9894e0cc3fb333147551c34143ec45e41e8c5d776b28a`
- csv_size_bytes (pre-update): `26430008`
- csv_backup_file: `brickovery_db_csv_backup_20260624_020815Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207371`
- items_db: `207998`
- items_missing_in_db: `7`
- codes_upstream: `84951`
- codes_db: `250163`
- codes_missing_in_db: `7`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260624_020815Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
