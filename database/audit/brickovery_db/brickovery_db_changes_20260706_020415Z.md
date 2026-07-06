# Brickovery DB backup & change audit — 20260706_020415Z

## Context
- created_at_utc: **20260706_020415Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3112` (id `28762962541`)
- commit: `329866fc5e00fb31ddb44c6a6d01d862ddaa1254`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `8fa272dd34565fb02287d9493154f078551a14ef36a4f8d716232491e19c1d3b`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260706_020415Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260706_020415Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `39ce8c3a0a127e9fdbb22bace39a67fb22b95038e8a26a01b7953721f794c205`
- csv_size_bytes (pre-update): `26469615`
- csv_backup_file: `brickovery_db_csv_backup_20260706_020415Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207737`
- items_db: `208400`
- items_missing_in_db: `15`
- codes_upstream: `85214`
- codes_db: `250843`
- codes_missing_in_db: `10`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260706_020415Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
