# Brickovery DB backup & change audit — 20261104_034654Z

## Context
- created_at_utc: **20261104_034654Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3824` (id `41768485406`)
- commit: `479ea33b82aa8ef83bb5b1baf0c593a56c2788f7`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `bd3c8942d5acafb3166b121f5a43d2ab0b86a1659f769b212903edf449419ea9`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261104_034654Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261104_034654Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `57468c1e756291dfb1632adef27f5bee4534c0766d444e9f53c7111a564f92fe`
- csv_size_bytes (pre-update): `26922980`
- csv_backup_file: `brickovery_db_csv_backup_20261104_034654Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212065`
- items_db: `213939`
- items_missing_in_db: `5`
- codes_upstream: `87150`
- codes_db: `258754`
- codes_missing_in_db: `4`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261104_034654Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
