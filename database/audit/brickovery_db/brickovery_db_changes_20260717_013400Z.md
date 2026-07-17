# Brickovery DB backup & change audit — 20260717_013400Z

## Context
- created_at_utc: **20260717_013400Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3161` (id `29547386334`)
- commit: `f4a98031471e05fd5974c46de70f15edf44b6077`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `273d935b60b8b811cd545a7cd2d2b1d281fee17ec3291b72f038f61eaf919a7b`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260717_013400Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260717_013400Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `11c24b0ca9f63a4f2d5014a4afb25db5b33117ccc50d7f0982ce75a017a446e0`
- csv_size_bytes (pre-update): `26487843`
- csv_backup_file: `brickovery_db_csv_backup_20260717_013400Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207877`
- items_db: `208557`
- items_missing_in_db: `13`
- codes_upstream: `85367`
- codes_db: `251159`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260717_013400Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
