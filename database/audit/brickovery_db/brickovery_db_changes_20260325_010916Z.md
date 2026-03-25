# Brickovery DB backup & change audit — 20260325_010916Z

## Context
- created_at_utc: **20260325_010916Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `413` (id `23519943722`)
- commit: `bbd4ce01d910d1f60005455cc2a4530f79dcae53`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `a8af4799366192b2241d5c48d91dcc5e8dceb551727b05569c245de9f70104bf`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260325_010916Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260325_010916Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `45722f5e5dce725457360dd37ddf1bb5553369ecd48e0fd8001c906f65981211`
- csv_size_bytes (pre-update): `26094790`
- csv_backup_file: `brickovery_db_csv_backup_20260325_010916Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `203781`
- items_db: `203871`
- items_missing_in_db: `3`
- codes_upstream: `84054`
- codes_db: `244298`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260325_010916Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
