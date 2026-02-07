# Brikick DB Post-Update Report

- created_at_utc: `20260207_180137Z`
- db_path: `database/brickovery.db`
- db_sha256: `1fa19b0acb481a2b9b68fddc78eda5d7b4c42df82d7376e9348f62eab3884905`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260207_180126Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260207_180126Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "8f2f7ba861800eb11f3d1ab35233a035ee54018988fc6a189ba75abf96842df4",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260207_180126Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202420,
    "items_db": 202417,
    "items_missing_in_db": 5,
    "codes_upstream": 83295,
    "codes_db": 242117,
    "codes_missing_in_db": 5,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "3e2742a60cc6fc5ed30ea6a68772ecee4e20fa2a32c9fb449eb3c04625f8f759",
  "csv_size_bytes": 25969769,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260207_180126Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202420,
  "items_db": 202417,
  "items_missing_in_db": 5,
  "codes_upstream": 83295,
  "codes_db": 242117,
  "codes_missing_in_db": 5,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 5,
  "db_inserted_codes": 5
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242127,
  "distinct_bl_part_id": 168277,
  "null_boid": 163961,
  "null_weight": 88651,
  "null_bk_part_id": 10,
  "null_bk_part_key": 10,
  "null_api_item_type": 10,
  "null_brikick_name": 10,
  "null_part_name": 88406,
  "null_element_id": 158890,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `163961`
- null_weight: `88651`
- corruption_pattern_count: `0`
