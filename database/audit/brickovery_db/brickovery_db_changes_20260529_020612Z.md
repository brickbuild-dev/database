# Brickovery DB backup & change audit — 20260529_020612Z

## Context
- created_at_utc: **20260529_020612Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2997` (id `26613458878`)
- commit: `e91f4eb9315bca9a72f64f9765bca80d240b0730`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `cf663bb6c3faed96bd35bb9682171d6a112c0c491ca8f783d91b6d47bf6a8ee2`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260529_020612Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260529_020612Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `3c3a122842a1557b3cfcceee5d78bea646dc3f37ac83eafd2fb9c2772dce5d83`
- csv_size_bytes (pre-update): `26316769`
- csv_backup_file: `brickovery_db_csv_backup_20260529_020612Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205959`
- items_db: `206519`
- items_missing_in_db: `13`
- codes_upstream: `84410`
- codes_db: `248193`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260529_020612Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
