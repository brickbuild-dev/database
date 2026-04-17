# Brickovery DB backup & change audit — 20260417_012610Z

## Context
- created_at_utc: **20260417_012610Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2896` (id `24542766516`)
- commit: `416309441e2531e6f2040e0e12bebcecd0ea84b3`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `c7a0e217cdc246ef731ae1074c33c44643a99ae1467c61b3f7d4199eba5d9964`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260417_012610Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260417_012610Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `8c0715ce7ddc975b591ddb537f231b6d7874852aca1bc4c233eff75c2309f8b2`
- csv_size_bytes (pre-update): `26194542`
- csv_backup_file: `brickovery_db_csv_backup_20260417_012610Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205213`
- items_db: `205553`
- items_missing_in_db: `8`
- codes_upstream: `84160`
- codes_db: `246076`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260417_012610Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
