# Brickovery DB backup & change audit — 20261127_080135Z

## Context
- created_at_utc: **20261127_080135Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `3908` (id `45961831882`)
- commit: `2eb58ebd80bbc3f90d727adad0f19c744694e822`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `6024b3a6f261ff8a8706eb413737e8ce73ff40a1defa76e5c837bc69aaf5a5ef`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20261127_080135Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20261127_080135Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `0ac9ba75783757e7cde05ada2723c71ca74c66384adc4f92e9d5e245731920b7`
- csv_size_bytes (pre-update): `26934995`
- csv_backup_file: `brickovery_db_csv_backup_20261127_080135Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `212217`
- items_db: `214094`
- items_missing_in_db: `9`
- codes_upstream: `87201`
- codes_db: `258961`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `4`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20261127_080135Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
