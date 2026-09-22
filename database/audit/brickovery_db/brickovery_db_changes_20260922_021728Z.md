# Brickovery DB backup & change audit — 20260922_021728Z

## Context
- created_at_utc: **20260922_021728Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3400` (id `35678451277`)
- commit: `b802c4be690372b86ac207cd51f21ecb41befbef`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `b1c42593e17bf303db20ef8d2bb02f815e63781fcfb97c453c6e22867b6de928`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260922_021728Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260922_021728Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `587b32953fa7bc438e9f43914ef96f855e9d9eddf8f0fd7ceb80a71029fa3f66`
- csv_size_bytes (pre-update): `26760962`
- csv_backup_file: `brickovery_db_csv_backup_20260922_021728Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211079`
- items_db: `211932`
- items_missing_in_db: `24`
- codes_upstream: `86709`
- codes_db: `255947`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260922_021728Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
