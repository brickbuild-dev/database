# Brickovery DB backup & change audit — 20260131_142158Z

## Context
- created_at_utc: **20260131_142158Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync upstream + update brickovery DB (semantic + chunked rebuild)`
- run: `53` (id `21545834072`)
- commit: `8cb95ecedde9bd64bb49bc66bd4242013d43a7dd`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `33a824b87a91f0659f4f1bea7e9944684cb2b9955ed9594855b927aae4627f3b`
- db_size_bytes (pre-update): `44621824`
- backup_file: `brickovery_db_backup_20260131_142158Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260131_142158Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `1db654e942cc03fbd48feb4a55801c22e40d9017b0de118b058a52345b78f596`
- csv_size_bytes (pre-update): `16164423`
- csv_backup_file: `brickovery_db_csv_backup_20260131_142158Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- (no context JSON provided)

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260131_142158Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
