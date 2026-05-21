# Brikick DB Post-Update Report

- created_at_utc: `20260521_020748Z`
- db_path: `database/brickovery.db`
- db_sha256: `8469978cb9374bf40a956b17448878060b719c66aa02248211af55c5bd8bea5f`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260521_020736Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260521_020736Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "d84da4b51b257d88f2d5f95b17a112ee34f72af3da1fc85b1030980603e67fda",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260521_020736Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205905,
    "items_db": 206397,
    "items_missing_in_db": 35,
    "codes_upstream": 84388,
    "codes_db": 247987,
    "codes_missing_in_db": 50,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "a5d45e248699bcd11cc94f1d75f3a635b51323c72b13c5362f60af6b61afef07",
  "csv_size_bytes": 26304936,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260521_020736Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205905,
  "items_db": 206397,
  "items_missing_in_db": 35,
  "codes_upstream": 84388,
  "codes_db": 247987,
  "codes_missing_in_db": 50,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 35,
  "db_inserted_codes": 50
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248072,
  "distinct_bl_part_id": 171958,
  "null_boid": 169897,
  "null_weight": 93511,
  "null_bk_part_id": 85,
  "null_bk_part_key": 85,
  "null_api_item_type": 85,
  "null_brikick_name": 85,
  "null_part_name": 94351,
  "null_element_id": 164835,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169897`
- null_weight: `93511`
- corruption_pattern_count: `0`
