# Brikick DB Post-Update Report

- created_at_utc: `20260909_025948Z`
- db_path: `database/brickovery.db`
- db_sha256: `4560889bac439e4506e36a1c9319f2106579b3d6109ba3e8c92bbc0aeeb3ffc6`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260909_025936Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260909_025936Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "216adf325ffcf3ed5c84954ccaa9f25e7c7a158a001411f2455390cc3fd428ac",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260909_025936Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210521,
    "items_db": 211361,
    "items_missing_in_db": 0,
    "codes_upstream": 86578,
    "codes_db": 255221,
    "codes_missing_in_db": 6,
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
  "csv_sha256": "d0f5ce3c4c3160c53282b1f2b6685a32dcdcbd59fa531b8542cc30a88339e210",
  "csv_size_bytes": 26720321,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260909_025936Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210521,
  "items_db": 211361,
  "items_missing_in_db": 0,
  "codes_upstream": 86578,
  "codes_db": 255221,
  "codes_missing_in_db": 6,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 0,
  "db_inserted_codes": 6
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255227,
  "distinct_bl_part_id": 176210,
  "null_boid": 177050,
  "null_weight": 99955,
  "null_bk_part_id": 6,
  "null_bk_part_key": 6,
  "null_api_item_type": 6,
  "null_brikick_name": 6,
  "null_part_name": 101506,
  "null_element_id": 171990,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177050`
- null_weight: `99955`
- corruption_pattern_count: `0`
