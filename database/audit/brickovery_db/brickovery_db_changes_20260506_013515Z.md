# Brickovery DB backup & change audit — 20260506_013515Z

## Context
- created_at_utc: **20260506_013515Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2955` (id `25411605202`)
- commit: `6f6ac926e271cac224f185500e54cef402be7fb8`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `a2b5eebd427516da73ee151c7c9ef138aa2eeed577d62362c444f0889efade12`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260506_013515Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260506_013515Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `52bad1934f0b10c5861963e9a5462be364b62409c9d77275eed519ba3e94ff09`
- csv_size_bytes (pre-update): `26264956`
- csv_backup_file: `brickovery_db_csv_backup_20260506_013515Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205672`
- items_db: `206057`
- items_missing_in_db: `32`
- codes_upstream: `84889`
- codes_db: `247293`
- codes_missing_in_db: `63`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260506_013515Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
