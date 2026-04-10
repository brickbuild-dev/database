# Brikick DB Post-Update Report

- created_at_utc: `20260410_012130Z`
- db_path: `database/brickovery.db`
- db_sha256: `5dbfba5bd424d0d65ece1b70723b46287df21b2be05256c2045ff30b7705229e`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260410_012119Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260410_012119Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "b3420d1be841d7e08a205ebd4cc729ac5fada63891fe16d2373d0f84e3442327",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260410_012119Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205150,
    "items_db": 204908,
    "items_missing_in_db": 576,
    "codes_upstream": 84124,
    "codes_db": 245350,
    "codes_missing_in_db": 54,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "b9c25d1c77ce6471b71566dbccd900120bd01f6470919a8df51ab2bd3d597eb5",
  "csv_size_bytes": 26153033,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260410_012119Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205150,
  "items_db": 204908,
  "items_missing_in_db": 576,
  "codes_upstream": 84124,
  "codes_db": 245350,
  "codes_missing_in_db": 54,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 576,
  "db_inserted_codes": 50
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 245976,
  "distinct_bl_part_id": 171133,
  "null_boid": 167806,
  "null_weight": 92129,
  "null_bk_part_id": 626,
  "null_bk_part_key": 626,
  "null_api_item_type": 626,
  "null_brikick_name": 626,
  "null_part_name": 92255,
  "null_element_id": 162739,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167806`
- null_weight: `92129`
- corruption_pattern_count: `0`
