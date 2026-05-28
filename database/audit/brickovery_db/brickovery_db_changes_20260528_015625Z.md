# Brickovery DB backup & change audit — 20260528_015625Z

## Context
- created_at_utc: **20260528_015625Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2995` (id `26549724021`)
- commit: `480dac765cf9c49dd1b42379fabec579ae761985`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `0d5426be530245fe5100cc11c4124e5a61647a74bc42c4e576208ae506d10a79`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260528_015625Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260528_015625Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `38bcf4e43766674e045c6f815900facd122d70c66a1305878f1c92ba907098ea`
- csv_size_bytes (pre-update): `26316344`
- csv_backup_file: `brickovery_db_csv_backup_20260528_015625Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205946`
- items_db: `206512`
- items_missing_in_db: `7`
- codes_upstream: `84410`
- codes_db: `248186`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260528_015625Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
