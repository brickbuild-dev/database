# Brickovery DB backup & change audit — 20260702_020908Z

## Context
- created_at_utc: **20260702_020908Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3105` (id `28560203567`)
- commit: `cc356b77f30df452b13332c5b860d8793cfc6e03`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `dd01d2ad1fa1beaf46632f48ec5a1a0cfe97955f59dd72a54d4393af4aaddc76`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260702_020908Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260702_020908Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `9357d62cd7d34b1edcac7b60fc4bda61ea8c887d3e973c32d5876c4aed191004`
- csv_size_bytes (pre-update): `26458656`
- csv_backup_file: `brickovery_db_csv_backup_20260702_020908Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207647`
- items_db: `208279`
- items_missing_in_db: `46`
- codes_upstream: `85164`
- codes_db: `250655`
- codes_missing_in_db: `28`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260702_020908Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
