# Brickovery DB backup & change audit — 20260219_051433Z

## Context
- created_at_utc: **20260219_051433Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `352` (id `22169476413`)
- commit: `0e0598d24796b335a2fd0a7663743d00d18c4cda`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `07272f6dce0f57ba63494f9e701d41fdc8c1830af70a996abcd93650d75889cd`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260219_051433Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260219_051433Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `4623d1dae577cae4d8999238de4ed455b0b04d1f5aa7c429c92d2df4523c33a6`
- csv_size_bytes (pre-update): `25984792`
- csv_backup_file: `brickovery_db_csv_backup_20260219_051433Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202550`
- items_db: `202531`
- items_missing_in_db: `26`
- codes_upstream: `83445`
- codes_db: `242377`
- codes_missing_in_db: `4`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260219_051433Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
