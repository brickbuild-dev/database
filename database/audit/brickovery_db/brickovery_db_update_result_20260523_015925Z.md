# Brikick DB Post-Update Report

- created_at_utc: `20260523_015925Z`
- db_path: `database/brickovery.db`
- db_sha256: `80f5bc08d1402e6c518bd3db986030d7fb32de739d99c820c50b43bf743b0f53`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260523_015914Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260523_015914Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "a0a3fe5219084f4ed224c7ae6d184d8d49d2fcab0bbd132b712b285cca96f192",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260523_015914Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205929,
    "items_db": 206452,
    "items_missing_in_db": 23,
    "codes_upstream": 84409,
    "codes_db": 248115,
    "codes_missing_in_db": 10,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "8bd5320055223104b48cabac4a8fad92df64ecbd17dad9e63a439b2b1c1b1710",
  "csv_size_bytes": 26312134,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260523_015914Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205929,
  "items_db": 206452,
  "items_missing_in_db": 23,
  "codes_upstream": 84409,
  "codes_db": 248115,
  "codes_missing_in_db": 10,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 23,
  "db_inserted_codes": 10
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248148,
  "distinct_bl_part_id": 172001,
  "null_boid": 169973,
  "null_weight": 93585,
  "null_bk_part_id": 33,
  "null_bk_part_key": 33,
  "null_api_item_type": 33,
  "null_brikick_name": 33,
  "null_part_name": 94427,
  "null_element_id": 164911,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169973`
- null_weight: `93585`
- corruption_pattern_count: `0`
