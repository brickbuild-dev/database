# Brickovery DB backup & change audit — 20260620_021257Z

## Context
- created_at_utc: **20260620_021257Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3081` (id `27856980521`)
- commit: `32527c5a91f720328f5871a9c6c41a5b1aeea651`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `fb670d0f1d11219108d1c48fe00816f9ea790a93d1bd8e33521418f83ccebb3a`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260620_021257Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260620_021257Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `5b2b55dc9433b76584594f60576bad1e1a80d13427a5ef04fc57c0585d499271`
- csv_size_bytes (pre-update): `26421516`
- csv_backup_file: `brickovery_db_csv_backup_20260620_021257Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207326`
- items_db: `207896`
- items_missing_in_db: `62`
- codes_upstream: `84901`
- codes_db: `250018`
- codes_missing_in_db: `2`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260620_021257Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
