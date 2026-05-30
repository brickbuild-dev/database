# Brickovery DB backup & change audit — 20260530_020017Z

## Context
- created_at_utc: **20260530_020017Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2999` (id `26671269310`)
- commit: `958369c8df95856ba297814a2cc63cd4c6a208dc`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `33e4e570a556bdb815ce8b3f7011daa07a06a249bebc2010c18c8c605c02109a`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260530_020017Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260530_020017Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `776bde7a58ef15d6b91ec4b01463d5530c8165bbdfbd08bbd68d6f7be8b8f66e`
- csv_size_bytes (pre-update): `26317459`
- csv_backup_file: `brickovery_db_csv_backup_20260530_020017Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205999`
- items_db: `206532`
- items_missing_in_db: `46`
- codes_upstream: `84410`
- codes_db: `248206`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260530_020017Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
