# Brickovery DB backup & change audit — 20260418_035507Z

## Context
- created_at_utc: **20260418_035507Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync BrickStore payload (semantic) + update DB (manual rebuild only)`
- run: `2918` (id `24596248578`)
- commit: `1a7beda115ecb6995b59da20f9566162185d51f8`
- actor: `github-actions[bot]`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `812ed90dd8db129072643cd90b7bba776949a92d49ad15579c29865a21dbd5c1`
- db_size_bytes (pre-update): `58519552`
- backup_file: `brickovery_db_backup_20260418_035507Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260418_035507Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `19fc94f24f562fbd7ad7e5455e313e99a60a04dbf2e150ad4c619622c54b6997`
- csv_size_bytes (pre-update): `26196012`
- csv_backup_file: `brickovery_db_csv_backup_20260418_035507Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- semantic_new_data: `True`
- items_upstream: `205223`
- items_db: `205577`
- items_missing_in_db: `1`
- codes_upstream: `84162`
- codes_db: `246102`
- codes_missing_in_db: `0`
- db_inserted_items: `0`
- db_inserted_codes: `0`
- unknown_color_tokens_count: `0`

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260418_035507Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
