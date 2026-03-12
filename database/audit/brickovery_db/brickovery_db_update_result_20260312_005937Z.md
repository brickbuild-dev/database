# Brikick DB Post-Update Report

- created_at_utc: `20260312_005937Z`
- db_path: `database/brickovery.db`
- db_sha256: `49b7df8050c7026206f2d6d6e652a8b7719c9a4838fe99247dda2b2ee79e2029`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260312_005926Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260312_005926Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "e0a0aa7229228d4033b8dd2fa6687a11cfe5386e83ade4070039e0f5807abf08",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260312_005926Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203467,
    "items_db": 203521,
    "items_missing_in_db": 13,
    "codes_upstream": 83938,
    "codes_db": 243837,
    "codes_missing_in_db": 3,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "bc8d2f230688a62856cee93db9aec626ad0dee85a6e860a0288968b92e56f425",
  "csv_size_bytes": 26068645,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260312_005926Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203467,
  "items_db": 203521,
  "items_missing_in_db": 13,
  "codes_upstream": 83938,
  "codes_db": 243837,
  "codes_missing_in_db": 3,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 13,
  "db_inserted_codes": 3
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243853,
  "distinct_bl_part_id": 169245,
  "null_boid": 165686,
  "null_weight": 90034,
  "null_bk_part_id": 16,
  "null_bk_part_key": 16,
  "null_api_item_type": 16,
  "null_brikick_name": 16,
  "null_part_name": 90132,
  "null_element_id": 160616,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165686`
- null_weight: `90034`
- corruption_pattern_count: `0`
