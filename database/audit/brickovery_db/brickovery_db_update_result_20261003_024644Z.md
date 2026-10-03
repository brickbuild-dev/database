# Brikick DB Post-Update Report

- created_at_utc: `20261003_024644Z`
- db_path: `database/brickovery.db`
- db_sha256: `37dfcbef885bd97e51369cec531537415b5ea660d1a05701a10985e027e64952`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261003_024633Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261003_024633Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "7569d2c39580a770b0f795480f13449e3da1dc5051e1ef2a81f48f2914ca8716",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261003_024633Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211401,
    "items_db": 213236,
    "items_missing_in_db": 1,
    "codes_upstream": 86749,
    "codes_db": 257657,
    "codes_missing_in_db": 2,
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
  "csv_sha256": "02b8e03c67b5b8d189fb9469036eb8d92c41fd664a93ce86c6030d132916798b",
  "csv_size_bytes": 26859681,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261003_024633Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211401,
  "items_db": 213236,
  "items_missing_in_db": 1,
  "codes_upstream": 86749,
  "codes_db": 257657,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 1,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 257660,
  "distinct_bl_part_id": 177988,
  "null_boid": 179481,
  "null_weight": 102332,
  "null_bk_part_id": 3,
  "null_bk_part_key": 3,
  "null_api_item_type": 3,
  "null_brikick_name": 3,
  "null_part_name": 103939,
  "null_element_id": 174423,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179481`
- null_weight: `102332`
- corruption_pattern_count: `0`
