# Brikick DB Post-Update Report

- created_at_utc: `20260812_010319Z`
- db_path: `database/brickovery.db`
- db_sha256: `46c804d4fc6c522a7ffd089d89f4a2267a8b75ce41f325cd7975c338d50894ad`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260812_010308Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260812_010308Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "5ca285b82647a610928925edbfb851154b905eb060974999e0ea59b568ac1fe0",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260812_010308Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209484,
    "items_db": 210223,
    "items_missing_in_db": 39,
    "codes_upstream": 86074,
    "codes_db": 253527,
    "codes_missing_in_db": 29,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "013e573eaa1dfb24a4c3bc6aab7235e4c967592e9385f64ba8c17c9af0c2e552",
  "csv_size_bytes": 26621379,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260812_010308Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209484,
  "items_db": 210223,
  "items_missing_in_db": 39,
  "codes_upstream": 86074,
  "codes_db": 253527,
  "codes_missing_in_db": 29,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 39,
  "db_inserted_codes": 27
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253593,
  "distinct_bl_part_id": 175311,
  "null_boid": 175416,
  "null_weight": 98401,
  "null_bk_part_id": 66,
  "null_bk_part_key": 66,
  "null_api_item_type": 66,
  "null_brikick_name": 66,
  "null_part_name": 99872,
  "null_element_id": 170356,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175416`
- null_weight: `98401`
- corruption_pattern_count: `0`
