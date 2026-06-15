# Brickovery DB backup & change audit — 20260615_023924Z

## Context
- created_at_utc: **20260615_023924Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3031` (id `27520550522`)
- commit: `939a8f8089ec3250e9d3ce0f9958447464367e43`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `4474e3fc4ccac26460a6e273f07d19b5f68097ab29e1823f34d5a8056a99d02e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260615_023924Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260615_023924Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `ef1874d32afbf29f3213f71f0a86ce6ec6e368db52b6d0d5e4cbc84ad92f27aa`
- csv_size_bytes (pre-update): `26399531`
- csv_backup_file: `brickovery_db_csv_backup_20260615_023924Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207146`
- items_db: `207661`
- items_missing_in_db: `96`
- codes_upstream: `84788`
- codes_db: `249638`
- codes_missing_in_db: `47`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260615_023924Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
