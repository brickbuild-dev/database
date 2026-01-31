# Brickovery DB backup & change audit — 20260131_140149Z

## Context
- created_at_utc: **20260131_140149Z**
- reason: **semantic_delta**
- repository: `brickbuild-dev/database`
- workflow: `Sync upstream + update brickovery DB (semantic + chunked rebuild)`
- run: `52` (id `21545584234`)
- commit: `36ebb4f04bfb3fbfc1dfa1c6483ad6c19cd13d27`
- actor: `brickbuild-dev`
- ref: `refs/heads/main`

## Backup (immutable)
- db_path: `database/brickovery.db`
- db_sha256 (pre-update): `cc96aa71718376c14a0041900f7f2b8dd6e6b52a659dd2bf093dd49c234fd1b5`
- db_size_bytes (pre-update): `44544000`
- backup_file: `brickovery_db_backup_20260131_140149Z.sqlite.gz`
- meta_file: `brickovery_db_backup_20260131_140149Z.meta.json`

## Optional CSV snapshot
- csv_sha256 (pre-update): `13fdef588f1b7b83ff8495da682fc93e694d69fe4250bdfcdf890e8a3afb3541`
- csv_size_bytes (pre-update): `16161604`
- csv_backup_file: `brickovery_db_csv_backup_20260131_140149Z.csv.gz`

## Intended change summary (from context JSON, if provided)
- (no context JSON provided)

## Restore procedure (emergency)
1) Stop any writers (workflows/scripts) that may modify the DB.
2) Download `database/backups/brickovery_db/brickovery_db_backup_20260131_140149Z.sqlite.gz` and decompress it:
   - `gzip -d brickovery_db_backup_...sqlite.gz`
3) Replace `database/brickovery.db` with the decompressed file.
4) Re-run export (mode export) to regenerate CSV and issues.

## Notes
- Backups and audit reports are immutable by design (new timestamped files per update).
- This DB is the Brikick critical dataset; treat backups as P0 artefacts.
