# Brikick DB Post-Update Report

- created_at_utc: `20260429_015525Z`
- db_path: `database/brickovery.db`
- db_sha256: `7d47fce67c614b0ed3bac80e0ac4b50b5ed154a99d15b0cc50e27680ccbf11b2`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260429_015514Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260429_015514Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "0166c7824217386eebb8a20db3558458cf640a2f4033a60ee72afe16ffe8f028",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260429_015514Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205373,
    "items_db": 205728,
    "items_missing_in_db": 19,
    "codes_upstream": 84327,
    "codes_db": 246376,
    "codes_missing_in_db": 53,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "41d9ffa8cb762c60d782e2d9edd3c46064669227bb79b12be8fc3c5498d3df90",
  "csv_size_bytes": 26211798,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260429_015514Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205373,
  "items_db": 205728,
  "items_missing_in_db": 19,
  "codes_upstream": 84327,
  "codes_db": 246376,
  "codes_missing_in_db": 53,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 19,
  "db_inserted_codes": 53
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246448,
  "distinct_bl_part_id": 171359,
  "null_boid": 168274,
  "null_weight": 92492,
  "null_bk_part_id": 72,
  "null_bk_part_key": 72,
  "null_api_item_type": 72,
  "null_brikick_name": 72,
  "null_part_name": 92727,
  "null_element_id": 163211,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168274`
- null_weight: `92492`
- corruption_pattern_count: `0`
