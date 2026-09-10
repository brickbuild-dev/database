# Brickovery DB backup & change audit — 20260910_035707Z

## Context
- created_at_utc: **20260910_035707Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3376` (id `34434868545`)
- commit: `582f9ace902141d453cb4d4597cfe8a0671cba9f`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `3393c9946995b3c4db4c3599c51d7548b1a0560210852b62fd45d93e31478839`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260910_035707Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260910_035707Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `dddf242f8c52a4285664eae6821929c9f7082d8bc884484360ad0f6359cf6df7`
- csv_size_bytes (pre-update): `26729324`
- csv_backup_file: `brickovery_db_csv_backup_20260910_035707Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210623`
- items_db: `211475`
- items_missing_in_db: `0`
- codes_upstream: `86608`
- codes_db: `255382`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260910_035707Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
