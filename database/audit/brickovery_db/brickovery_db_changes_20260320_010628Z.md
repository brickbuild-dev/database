# Brickovery DB backup & change audit — 20260320_010628Z

## Context
- created_at_utc: **20260320_010628Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `403` (id `23324554843`)
- commit: `90c8b3f3844c65165d480f78560901cb346df2a8`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `09b7d11d2860f552f029ff747161e0c56e8ca74ce7e7cddff6c5a226fb62b226`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260320_010628Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260320_010628Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `128bbd37a8d7be8c62dfd7dcc0c7a70d723017d0f2a298e4d7feda27bb94b9d3`
- csv_size_bytes (pre-update): `26087034`
- csv_backup_file: `brickovery_db_csv_backup_20260320_010628Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203699`
- items_db: `203768`
- items_missing_in_db: `7`
- codes_upstream: `84031`
- codes_db: `244157`
- codes_missing_in_db: `18`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260320_010628Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
