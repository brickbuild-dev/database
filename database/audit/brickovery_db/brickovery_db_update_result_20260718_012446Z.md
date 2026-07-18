# Brikick DB Post-Update Report

- created_at_utc: `20260718_012446Z`
- db_path: `database/brickovery.db`
- db_sha256: `83f5e0ab4b71f133d037cb2e48d7906e23d54a613db11c572295b5509a6d7132`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260718_012435Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260718_012435Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "cf27b1dae613291b150596277c0b0eba988649f363f6ebf2f0492c5d936348b8",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260718_012435Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207879,
    "items_db": 208570,
    "items_missing_in_db": 7,
    "codes_upstream": 85368,
    "codes_db": 251173,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "1b252a23536457e02980d3a357bf6fa2f01fb299841c2d7830e00b5445783a12",
  "csv_size_bytes": 26488652,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260718_012435Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207879,
  "items_db": 208570,
  "items_missing_in_db": 7,
  "codes_upstream": 85368,
  "codes_db": 251173,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 7,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251181,
  "distinct_bl_part_id": 173797,
  "null_boid": 173005,
  "null_weight": 96352,
  "null_bk_part_id": 8,
  "null_bk_part_key": 8,
  "null_api_item_type": 8,
  "null_brikick_name": 8,
  "null_part_name": 97460,
  "null_element_id": 167944,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `173005`
- null_weight: `96352`
- corruption_pattern_count: `0`
