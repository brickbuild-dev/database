# Brickovery DB backup & change audit — 20260618_023708Z

## Context
- created_at_utc: **20260618_023708Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3066` (id `27732800708`)
- commit: `67930bddc690e51b5e201846c2c176e984f0f30c`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `3b70607450ad809f52da412d063c9eac4b44d2f1259a83fc28ba000be36973a5`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260618_023708Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260618_023708Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `1953c1889eda860b86f29698b7940445a95afe57376ed83db7025fbfabc23ec8`
- csv_size_bytes (pre-update): `26418204`
- csv_backup_file: `brickovery_db_csv_backup_20260618_023708Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207264`
- items_db: `207866`
- items_missing_in_db: `17`
- codes_upstream: `84898`
- codes_db: `249961`
- codes_missing_in_db: `24`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260618_023708Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
