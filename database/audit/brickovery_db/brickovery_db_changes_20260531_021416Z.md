# Brickovery DB backup & change audit — 20260531_021416Z

## Context
- created_at_utc: **20260531_021416Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3001` (id `26700711574`)
- commit: `0d6989da8dae75346c96ea6f136a9563d8713d01`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `43be680b153f16bcf06f06af51aa42b927967ed5e33140c88a838404f9100aaf`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260531_021416Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260531_021416Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `175deb154ee9102af54481dc657ee6b0976727928e15d218c740250fc55b1f2f`
- csv_size_bytes (pre-update): `26319992`
- csv_backup_file: `brickovery_db_csv_backup_20260531_021416Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `206048`
- items_db: `206578`
- items_missing_in_db: `54`
- codes_upstream: `84410`
- codes_db: `248252`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260531_021416Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
