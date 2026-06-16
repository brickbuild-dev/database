# Brikick DB Post-Update Report

- created_at_utc: `20260616_024345Z`
- db_path: `database/brickovery.db`
- db_sha256: `8bf5beb47b94668724a2fe1cfa21c32323931288213dbfb4caa8e849d6f0fdd0`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260616_024334Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260616_024334Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "368222822f03ddcdcb21faae81576a7b1deb2cea131fdc55a7212d9b03a04476",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260616_024334Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207204,
    "items_db": 207757,
    "items_missing_in_db": 64,
    "codes_upstream": 84849,
    "codes_db": 249780,
    "codes_missing_in_db": 59,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "cb0db65eed212613f0e37d41556fdbf0946e4c42a8ed43f9cd38b590ad9eec26",
  "csv_size_bytes": 26407760,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260616_024334Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207204,
  "items_db": 207757,
  "items_missing_in_db": 64,
  "codes_upstream": 84849,
  "codes_db": 249780,
  "codes_missing_in_db": 59,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 64,
  "db_inserted_codes": 53
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 249897,
  "distinct_bl_part_id": 173080,
  "null_boid": 171721,
  "null_weight": 95237,
  "null_bk_part_id": 117,
  "null_bk_part_key": 117,
  "null_api_item_type": 117,
  "null_brikick_name": 117,
  "null_part_name": 96176,
  "null_element_id": 166660,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171721`
- null_weight: `95237`
- corruption_pattern_count: `0`
