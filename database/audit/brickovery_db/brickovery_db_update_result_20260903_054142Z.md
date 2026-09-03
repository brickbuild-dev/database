# Brikick DB Post-Update Report

- created_at_utc: `20260903_054142Z`
- db_path: `database/brickovery.db`
- db_sha256: `b7043a592c3cff65a73a8bd07728813413ef76417872878ac85299edced776ef`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260903_054130Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260903_054130Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "0165c8c9fb5b67d396547efeaf9ebf017102dfaecda3d9a35c2806944a0788a4",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260903_054130Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210204,
    "items_db": 211023,
    "items_missing_in_db": 2,
    "codes_upstream": 86394,
    "codes_db": 254708,
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
  "csv_sha256": "058b8fccb6f2900f4c48d268c15a3b63f59a6c941f1d1b6c25831eb4eea2b01f",
  "csv_size_bytes": 26690486,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260903_054130Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210204,
  "items_db": 211023,
  "items_missing_in_db": 2,
  "codes_upstream": 86394,
  "codes_db": 254708,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 2,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254712,
  "distinct_bl_part_id": 175915,
  "null_boid": 176535,
  "null_weight": 99478,
  "null_bk_part_id": 4,
  "null_bk_part_key": 4,
  "null_api_item_type": 4,
  "null_brikick_name": 4,
  "null_part_name": 100991,
  "null_element_id": 171475,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176535`
- null_weight: `99478`
- corruption_pattern_count: `0`
