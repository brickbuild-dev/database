# Brikick DB Post-Update Report

- created_at_utc: `20260221_045352Z`
- db_path: `database/brickovery.db`
- db_sha256: `e02e5dafbba10d6411b8a8235dd33df17da86806f6e3de3d61bdc2c5c81b5428`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260221_045341Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260221_045341Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "cb9d836afd5571786397cc4398b2df11f84661e662685058710afed9dafc3477",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260221_045341Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202591,
    "items_db": 202594,
    "items_missing_in_db": 5,
    "codes_upstream": 83533,
    "codes_db": 242445,
    "codes_missing_in_db": 89,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "b72fe57077490b07413276eb00a1dd6dac2b2a23c58cfef736a5ed5e431bfbad",
  "csv_size_bytes": 25988624,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260221_045341Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202591,
  "items_db": 202594,
  "items_missing_in_db": 5,
  "codes_upstream": 83533,
  "codes_db": 242445,
  "codes_missing_in_db": 89,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 5,
  "db_inserted_codes": 89
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242539,
  "distinct_bl_part_id": 168439,
  "null_boid": 164372,
  "null_weight": 88939,
  "null_bk_part_id": 94,
  "null_bk_part_key": 94,
  "null_api_item_type": 94,
  "null_brikick_name": 94,
  "null_part_name": 88818,
  "null_element_id": 159302,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `164372`
- null_weight: `88939`
- corruption_pattern_count: `0`
