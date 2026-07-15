# Brickovery DB backup & change audit — 20260715_012011Z

## Context
- created_at_utc: **20260715_012011Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3133` (id `29381086945`)
- commit: `2d3a8858ee124ecc8c80e50ceb655bc5513a0b39`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `03237635b0eb77ecb78a1c1f12677d7e8c35f0f3431fefe965f04389ca4a2a9a`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260715_012011Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260715_012011Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `a7cc52e109be7ac53b0ee53ff9f0d6997534c3e50de1504a61c37f007ebb5340`
- csv_size_bytes (pre-update): `26486284`
- csv_backup_file: `brickovery_db_csv_backup_20260715_012011Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207860`
- items_db: `208534`
- items_missing_in_db: `17`
- codes_upstream: `85364`
- codes_db: `251132`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260715_012011Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
