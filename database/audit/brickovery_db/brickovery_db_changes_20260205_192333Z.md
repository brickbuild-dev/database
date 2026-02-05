# Brickovery DB backup & change audit — 20260205_192333Z

## Context
- created_at_utc: **20260205_192333Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `94` (id `21725269738`)
- commit: `c3dacbca5ef6f420244acd8d6a00af8be7dc1e7f`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `fdad5cc332080eea453c4d1ebfec108004a5ef3c4c37d25d9b4b5f48fbc36953`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260205_192333Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260205_192333Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `b45596819bbdb4ecac49e595085b086d3e313be8f6bf11d352a6696f710442e9`
- csv_size_bytes (pre-update): `25308588`
- csv_backup_file: `brickovery_db_csv_backup_20260205_192333Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `202401`
- items_db: `202400`
- items_missing_in_db: `1`
- codes_upstream: `83280`
- codes_db: `242093`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260205_192333Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
