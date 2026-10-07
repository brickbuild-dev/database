# Brikick DB Post-Update Report

- created_at_utc: `20261007_030831Z`
- db_path: `database/brickovery.db`
- db_sha256: `58acd4159fe1c466252742f07dbf6545a8bb0ef42a713652a8606b08ce900d5b`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261007_030821Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261007_030821Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "a97e73265ba75942a792fbff9c0ae2c287217209967402569c962e4f7e046531",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261007_030821Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211509,
    "items_db": 213329,
    "items_missing_in_db": 22,
    "codes_upstream": 86885,
    "codes_db": 257857,
    "codes_missing_in_db": 26,
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
  "csv_sha256": "36a8d9f84d98e41d7bbbbae8b7c59c168ef76ae3f581813c1335b826cc28d398",
  "csv_size_bytes": 26871299,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261007_030821Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211509,
  "items_db": 213329,
  "items_missing_in_db": 22,
  "codes_upstream": 86885,
  "codes_db": 257857,
  "codes_missing_in_db": 26,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 22,
  "db_inserted_codes": 24
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 257903,
  "distinct_bl_part_id": 178093,
  "null_boid": 179723,
  "null_weight": 102522,
  "null_bk_part_id": 46,
  "null_bk_part_key": 46,
  "null_api_item_type": 46,
  "null_brikick_name": 46,
  "null_part_name": 104182,
  "null_element_id": 174666,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179723`
- null_weight: `102522`
- corruption_pattern_count: `0`
