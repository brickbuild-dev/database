# Brikick DB Post-Update Report

- created_at_utc: `20260707_020036Z`
- db_path: `database/brickovery.db`
- db_sha256: `62cbca56f7e0083b50bca36c2d06f12cc1b778f3102be506b113902171f42814`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260707_020024Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260707_020024Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "83e5f3e889d9d7e6c70f1c6a7e8c74cdd97fde81793d07095b10360169dfab1c",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260707_020024Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207740,
    "items_db": 208415,
    "items_missing_in_db": 3,
    "codes_upstream": 85214,
    "codes_db": 250868,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "94c808b3939e33a1a106e55aea78b34c9868ceba6a16d8b9c3207cbe8fe3384b",
  "csv_size_bytes": 26471082,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260707_020024Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207740,
  "items_db": 208415,
  "items_missing_in_db": 3,
  "codes_upstream": 85214,
  "codes_db": 250868,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 3,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250871,
  "distinct_bl_part_id": 173641,
  "null_boid": 172695,
  "null_weight": 96145,
  "null_bk_part_id": 3,
  "null_bk_part_key": 3,
  "null_api_item_type": 3,
  "null_brikick_name": 3,
  "null_part_name": 97150,
  "null_element_id": 167634,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172695`
- null_weight: `96145`
- corruption_pattern_count: `0`
