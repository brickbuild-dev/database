# Brickovery DB backup & change audit — 20260524_020551Z

## Context
- created_at_utc: **20260524_020551Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2987` (id `26349128774`)
- commit: `efbe130ed7cccd9cba4907a0dd4b98dcbd030631`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `65c182e68396454e07a9e639f59c8578e4cfed1b6efb46b7fb25f33f2cccafda`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260524_020551Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260524_020551Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `51e27908e5a537992ea8ef101d9cceaee7c00e7f300179c8eac8525e9086ec82`
- csv_size_bytes (pre-update): `26314047`
- csv_backup_file: `brickovery_db_csv_backup_20260524_020551Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205931`
- items_db: `206475`
- items_missing_in_db: `5`
- codes_upstream: `84409`
- codes_db: `248148`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260524_020551Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
