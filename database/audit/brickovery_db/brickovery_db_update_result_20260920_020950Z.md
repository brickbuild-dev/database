# Brikick DB Post-Update Report

- created_at_utc: `20260920_020950Z`
- db_path: `database/brickovery.db`
- db_sha256: `1306298cdbc627dec9bc709731868a9f6073a0068269bc60af0e1aaeed574d8b`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260920_020938Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260920_020938Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "743e4922f9c479344cfe7607b2fd71643bbd5f95efa546bd0c301d9d3398a10f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260920_020938Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210830,
    "items_db": 211656,
    "items_missing_in_db": 42,
    "codes_upstream": 86703,
    "codes_db": 255666,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [
      "Royal Blue",
      "Speckle Copper",
      "Speckle Gold",
      "Speckle Silver"
    ],
    "unknown_color_tokens_count": 4,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "4410310764e220b6dd554d5f512ac5ac782d3e5e2473f3aa5af573496aaf7a17",
  "csv_size_bytes": 26746001,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260920_020938Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210830,
  "items_db": 211656,
  "items_missing_in_db": 42,
  "codes_upstream": 86703,
  "codes_db": 255666,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 42,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255708,
  "distinct_bl_part_id": 176510,
  "null_boid": 177531,
  "null_weight": 100397,
  "null_bk_part_id": 42,
  "null_bk_part_key": 42,
  "null_api_item_type": 42,
  "null_brikick_name": 42,
  "null_part_name": 101987,
  "null_element_id": 172471,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177531`
- null_weight: `100397`
- corruption_pattern_count: `0`
