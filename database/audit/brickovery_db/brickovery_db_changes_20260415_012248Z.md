# Brickovery DB backup & change audit — 20260415_012248Z

## Context
- created_at_utc: **20260415_012248Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2892` (id `24431336816`)
- commit: `70c4e6268169a3f57a9c5ec51109fbf155c5257c`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `ef5cce1cd32e21f5ad111810c500b1ff08184406095047a719571080097f2c48`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260415_012248Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260415_012248Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `e5538294f548585cb5c9b4fc911e4d862d23a2d38c115cf6f489e3a3a4dfc61f`
- csv_size_bytes (pre-update): `26192947`
- csv_backup_file: `brickovery_db_csv_backup_20260415_012248Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205201`
- items_db: `205537`
- items_missing_in_db: `12`
- codes_upstream: `84156`
- codes_db: `246049`
- codes_missing_in_db: `7`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260415_012248Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
