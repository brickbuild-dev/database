# Brikick DB Post-Update Report

- created_at_utc: `20261021_022552Z`
- db_path: `database/brickovery.db`
- db_sha256: `7bdce680c767f4c4e46e6672b7dcdc68617e309b0356043ba55631ce9455bc06`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261021_022540Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261021_022540Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "f8cff9dae7cdaa102889a9e890117b91ab0ae8e8bd1035b95c23a7206deb9ca4",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261021_022540Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211706,
    "items_db": 213554,
    "items_missing_in_db": 19,
    "codes_upstream": 87018,
    "codes_db": 258240,
    "codes_missing_in_db": 3,
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
  "csv_sha256": "1d23f66fe74c9ebc8c4feb22bc293abae118c77e36778d2c8cad0472964d6460",
  "csv_size_bytes": 26893617,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261021_022540Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211706,
  "items_db": 213554,
  "items_missing_in_db": 19,
  "codes_upstream": 87018,
  "codes_db": 258240,
  "codes_missing_in_db": 3,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 19,
  "db_inserted_codes": 3
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258262,
  "distinct_bl_part_id": 178305,
  "null_boid": 180082,
  "null_weight": 102824,
  "null_bk_part_id": 22,
  "null_bk_part_key": 22,
  "null_api_item_type": 22,
  "null_brikick_name": 22,
  "null_part_name": 104541,
  "null_element_id": 175025,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180082`
- null_weight: `102824`
- corruption_pattern_count: `0`
