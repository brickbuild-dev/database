# Brickovery DB backup & change audit — 20260905_015055Z

## Context
- created_at_utc: **20260905_015055Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3333` (id `33937037854`)
- commit: `6a49e8eb933dde112b24f5e13dd6cd180917d53e`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `eed833bf13e7045492151653345517b84889976a4dc60b1f99d2b82eea3a8576`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260905_015055Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260905_015055Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `199a9a628e7603dbfda0f5cd9dcbcad937896ad6b8ab159268ed6878439f297a`
- csv_size_bytes (pre-update): `26693730`
- csv_backup_file: `brickovery_db_csv_backup_20260905_015055Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210283`
- items_db: `211068`
- items_missing_in_db: `51`
- codes_upstream: `86414`
- codes_db: `254763`
- codes_missing_in_db: `11`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260905_015055Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
