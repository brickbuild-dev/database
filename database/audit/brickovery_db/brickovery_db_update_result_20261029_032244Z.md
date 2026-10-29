# Brikick DB Post-Update Report

- created_at_utc: `20261029_032244Z`
- db_path: `database/brickovery.db`
- db_sha256: `4416aaeddb8d2517575efdeac3abf369654cfe5e69541b7e70bc5f70a08ece38`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261029_032232Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261029_032232Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "e943f64063abe3cd0babaca73c10b1266375945603f7731573fdda2c78e15dfd",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261029_032232Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211928,
    "items_db": 213732,
    "items_missing_in_db": 73,
    "codes_upstream": 87093,
    "codes_db": 258471,
    "codes_missing_in_db": 23,
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
  "csv_sha256": "e31496253c9c17f3a941650808fa707943a14eb953375999a25635228d4e7387",
  "csv_size_bytes": 26906771,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261029_032232Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211928,
  "items_db": 213732,
  "items_missing_in_db": 73,
  "codes_upstream": 87093,
  "codes_db": 258471,
  "codes_missing_in_db": 23,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 73,
  "db_inserted_codes": 23
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258567,
  "distinct_bl_part_id": 178521,
  "null_boid": 180387,
  "null_weight": 103127,
  "null_bk_part_id": 96,
  "null_bk_part_key": 96,
  "null_api_item_type": 96,
  "null_brikick_name": 96,
  "null_part_name": 104846,
  "null_element_id": 175330,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180387`
- null_weight: `103127`
- corruption_pattern_count: `0`
