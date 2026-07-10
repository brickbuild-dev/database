# Brickovery DB backup & change audit — 20260710_013706Z

## Context
- created_at_utc: **20260710_013706Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3120` (id `29062502519`)
- commit: `da6964c0dd600a6b80c051db024f22873983cdfb`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `739214102fa6dc6f16d97c703797bdacfa2260c2ee48a07b1e831948e43e474e`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260710_013706Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260710_013706Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `ff92625c74fc4cc88f81a8d1611d89848479b0c82f1618e9251edf69cb18cb64`
- csv_size_bytes (pre-update): `26473907`
- csv_backup_file: `brickovery_db_csv_backup_20260710_013706Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `207825`
- items_db: `208438`
- items_missing_in_db: `66`
- codes_upstream: `85278`
- codes_db: `250917`
- codes_missing_in_db: `35`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260710_013706Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
