# Brickovery DB backup & change audit — 20260719_013029Z

## Context
- created_at_utc: **20260719_013029Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3165` (id `29668502070`)
- commit: `63169bafd4df112d52fdad488bc287897cff029d`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `29a4fbdae99d2f966d65357a154bdc4015ff966b966e5f145d232a5d172dc3b1`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260719_013029Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260719_013029Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `74dd033e0a3e9c2c38f67ac43cda49edd78eb1071e2c3a859a00592a4028d6cf`
- csv_size_bytes (pre-update): `26489118`
- csv_backup_file: `brickovery_db_csv_backup_20260719_013029Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207890`
- items_db: `208577`
- items_missing_in_db: `11`
- codes_upstream: `85372`
- codes_db: `251181`
- codes_missing_in_db: `3`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260719_013029Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
