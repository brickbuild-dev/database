# Brickovery DB backup & change audit — 20260708_012926Z

## Context
- created_at_utc: **20260708_012926Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3116` (id `28910622921`)
- commit: `192a8e0b952363e035218a4a0a05f9363d397b23`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `3958b9917853815492cf784d1ed912597fc01bc8bd37578a70f91dc0d98ffd12`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260708_012926Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260708_012926Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `b77323f73c532b04e2c8fda4f013872f9b856c7602b3973c0d5ff3fcbda6ff98`
- csv_size_bytes (pre-update): `26471253`
- csv_backup_file: `brickovery_db_csv_backup_20260708_012926Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207753`
- items_db: `208418`
- items_missing_in_db: `13`
- codes_upstream: `85226`
- codes_db: `250871`
- codes_missing_in_db: `12`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260708_012926Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
