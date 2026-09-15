# Brickovery DB backup & change audit — 20260915_022059Z

## Context
- created_at_utc: **20260915_022059Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3386` (id `34920201485`)
- commit: `c79593743561e2542280a515ccfaf57d309d5ea3`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `025535dec86c2d63bbc81af548b74e1d145c3e43970a9d21a812893c895ffbd5`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260915_022059Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260915_022059Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `4dc75152531ec4c9ad89e7be1d4c0bae651c5e17cfb26d1bc66dda8a6bdddb5f`
- csv_size_bytes (pre-update): `26736710`
- csv_backup_file: `brickovery_db_csv_backup_20260915_022059Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210756`
- items_db: `211553`
- items_missing_in_db: `65`
- codes_upstream: `86665`
- codes_db: `255509`
- codes_missing_in_db: `11`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260915_022059Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
