# Brickovery DB backup & change audit — 20261014_023733Z

## Context
- created_at_utc: **20261014_023733Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3753` (id `38501071879`)
- commit: `0fefe86f445858d5ca6f3ee305e94fcc372dd91c`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `15e6df78ab38292df4c824b1d9954456b9c4fcf63d32cd4ad76afd4149e0c963`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261014_023733Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261014_023733Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `1c46907d3c8626a37df62dfbb91b3aa44533cb8deba840b8951d255065ddd69e`
- csv_size_bytes (pre-update): `26885604`
- csv_backup_file: `brickovery_db_csv_backup_20261014_023733Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `211604`
- items_db: `213454`
- items_missing_in_db: `4`
- codes_upstream: `86980`
- codes_db: `258101`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261014_023733Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
