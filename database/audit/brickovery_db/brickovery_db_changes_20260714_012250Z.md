# Brickovery DB backup & change audit — 20260714_012250Z

## Context
- created_at_utc: **20260714_012250Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3131` (id `29298106243`)
- commit: `192cd8bbcc11e575ecf70e70cc29763a31051574`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `3a607e7b5498bf97303b64c9240cc8f8776ef00c2e64ea7c528dab4ccf201aa0`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260714_012250Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260714_012250Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `9691362ebcc4c17d5ae300cd6a06d4c92e7f8424e03b4ecaf0ef597fae68c081`
- csv_size_bytes (pre-update): `26486050`
- csv_backup_file: `brickovery_db_csv_backup_20260714_012250Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207845`
- items_db: `208531`
- items_missing_in_db: `3`
- codes_upstream: `85356`
- codes_db: `251128`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260714_012250Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
