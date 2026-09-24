# Brickovery DB backup & change audit — 20260924_020311Z

## Context
- created_at_utc: **20260924_020311Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3404` (id `35945091409`)
- commit: `9fdcfe3c9118118f565ff8b2883b396aaa6969cb`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `45a392638bb1d820530962ce38754fb88d3b992e7fe6119f238a0b6dd8179394`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260924_020311Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260924_020311Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `57a5f2ef33447d40200869fad1e4ae1dc865c9b2aa8479b6fe819a29ea79bd6c`
- csv_size_bytes (pre-update): `26764375`
- csv_backup_file: `brickovery_db_csv_backup_20260924_020311Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211137`
- items_db: `211995`
- items_missing_in_db: `58`
- codes_upstream: `86709`
- codes_db: `256012`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260924_020311Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
