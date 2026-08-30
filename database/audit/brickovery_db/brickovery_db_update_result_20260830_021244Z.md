# Brikick DB Post-Update Report

- created_at_utc: `20260830_021244Z`
- db_path: `database/brickovery.db`
- db_sha256: `80e50fd8dc2ed0fb22cdd3f49b414fc48ae8a37bcf52bae97788561370a448f0`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260830_021232Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260830_021232Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "838d36f026adf34e2d7a1e55ebcad41e0c9081e771ce9b125e7acb83e88f761c",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260830_021232Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209910,
    "items_db": 210711,
    "items_missing_in_db": 18,
    "codes_upstream": 86351,
    "codes_db": 254360,
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
  "csv_sha256": "0fde7e9ed443ec705262a4c08fde472901fa167d147c2c2e1d9a5ccfe8eb3b0b",
  "csv_size_bytes": 26670052,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260830_021232Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209910,
  "items_db": 210711,
  "items_missing_in_db": 18,
  "codes_upstream": 86351,
  "codes_db": 254360,
  "codes_missing_in_db": 6,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 18,
  "db_inserted_codes": 3
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254381,
  "distinct_bl_part_id": 175750,
  "null_boid": 176204,
  "null_weight": 99160,
  "null_bk_part_id": 21,
  "null_bk_part_key": 21,
  "null_api_item_type": 21,
  "null_brikick_name": 21,
  "null_part_name": 100660,
  "null_element_id": 171144,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176204`
- null_weight: `99160`
- corruption_pattern_count: `0`
