# Brickovery DB backup & change audit — 20260212_141833Z

## Context
- created_at_utc: **20260212_141833Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `338` (id `21950228226`)
- commit: `2b5682ad3d8ba507d444a34f8deec75ab088c762`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `35db7c3cec73a2ba4a9b1c7866c4393c78c2d75f5b5fbe9f64c424db76eb35d2`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260212_141833Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260212_141833Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `5fe1487b9ea3bd776820b32e4021d805da0b0aae9885533cfb876ae9501d3f46`
- csv_size_bytes (pre-update): `25973770`
- csv_backup_file: `brickovery_db_csv_backup_20260212_141833Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202460`
- items_db: `202463`
- items_missing_in_db: `1`
- codes_upstream: `83313`
- codes_db: `242185`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260212_141833Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
