# Brickovery DB backup & change audit — 20260306_011058Z

## Context
- created_at_utc: **20260306_011058Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `375` (id `22744282888`)
- commit: `eb41eef5a6680e9d96ff73c09e57a28eabd51ca5`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `f457c8efb1cd3b212fd5a2831bde640d03071721dfe7100f75705c317f29de50`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260306_011058Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260306_011058Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `3393f1e8bf25ebf3e3cc26dddbbb396a666b9786cd835b1d4027a0faa4dd86e8`
- csv_size_bytes (pre-update): `26052099`
- csv_backup_file: `brickovery_db_csv_backup_20260306_011058Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203324`
- items_db: `203361`
- items_missing_in_db: `16`
- codes_upstream: `83807`
- codes_db: `243550`
- codes_missing_in_db: `10`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260306_011058Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
