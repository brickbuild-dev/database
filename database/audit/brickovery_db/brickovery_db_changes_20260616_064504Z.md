# Brickovery DB backup & change audit — 20260616_064504Z

## Context
- created_at_utc: **20260616_064504Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3062` (id `27599239019`)
- commit: `6bec7bff621003febce83fe4020e2ac76bad4f52`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `78ea58d52418d5273d803ae46cbdb19a2cfd50a2f18913e3e596490e030a46d2`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260616_064504Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260616_064504Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8fa90f676fddec4455153912f7483425f366c83e33ddd096f4815d1581a204f7`
- csv_size_bytes (pre-update): `26414504`
- csv_backup_file: `brickovery_db_csv_backup_20260616_064504Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207205`
- items_db: `207821`
- items_missing_in_db: `1`
- codes_upstream: `84851`
- codes_db: `249897`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260616_064504Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
