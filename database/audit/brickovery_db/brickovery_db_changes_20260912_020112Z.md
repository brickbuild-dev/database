# Brickovery DB backup & change audit — 20260912_020112Z

## Context
- created_at_utc: **20260912_020112Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3380` (id `34666148569`)
- commit: `f521f64bbb8edb0f37cb54deb42c27fb77f9a7df`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `bac8a74987745c19ff58f6928aedfabdadb784afcd909129eed6f260666f7674`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260912_020112Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260912_020112Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `b3dfe66f04dd3a225c446d416fa20a4389150e026c9d3a088bdbaeac00274c34`
- csv_size_bytes (pre-update): `26730014`
- csv_backup_file: `brickovery_db_csv_backup_20260912_020112Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210657`
- items_db: `211478`
- items_missing_in_db: `38`
- codes_upstream: `86623`
- codes_db: `255394`
- codes_missing_in_db: `8`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260912_020112Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
