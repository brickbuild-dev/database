# Brickovery DB backup & change audit — 20260527_021353Z

## Context
- created_at_utc: **20260527_021353Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2993` (id `26486425065`)
- commit: `226a8783aaedff2b4b09eb6e1898f060f29a09eb`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `1b1c7954c1a2ed3f240cf754bddd39ef3d09aef514c932e9526a992249a1f1fe`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260527_021353Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260527_021353Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `a15a2fdfebc07ac2884de1c1aad053a90712821424f59b3593c4d7f754226d1a`
- csv_size_bytes (pre-update): `26315555`
- csv_backup_file: `brickovery_db_csv_backup_20260527_021353Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205942`
- items_db: `206500`
- items_missing_in_db: `12`
- codes_upstream: `84410`
- codes_db: `248173`
- codes_missing_in_db: `1`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260527_021353Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
