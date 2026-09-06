# Brickovery DB backup & change audit — 20260906_014515Z

## Context
- created_at_utc: **20260906_014515Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3349` (id `34004401771`)
- commit: `80fc7af34cdb5d0eaf49f1986e5a203e3fba5d85`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `594e05a0d2a0ad33164d59a908fe2fa3b574cd37cd22a2dcf5fdc97e18d6dfd1`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260906_014515Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260906_014515Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `9978ef80151b40cc81084e34df828f1df435c4ef50b87a355ad16d725aefce82`
- csv_size_bytes (pre-update): `26697598`
- csv_backup_file: `brickovery_db_csv_backup_20260906_014515Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `210311`
- items_db: `211123`
- items_missing_in_db: `24`
- codes_upstream: `86432`
- codes_db: `254829`
- codes_missing_in_db: `15`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260906_014515Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
