# Brikick DB Post-Update Report

- created_at_utc: `20260913_015137Z`
- db_path: `database/brickovery.db`
- db_sha256: `6d8271016fb4fdefbf784771dbd1163c1b843c3e77363da4afa040e225f52162`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260913_015127Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260913_015127Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "741b0f3936fd2e4ef7f1b457c93d78ad659b6e882909bc9c0c7b9e987b1c5f1c",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260913_015127Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210675,
    "items_db": 211516,
    "items_missing_in_db": 20,
    "codes_upstream": 86640,
    "codes_db": 255440,
    "codes_missing_in_db": 17,
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
  "csv_sha256": "dd3f75ff215494904f2baa09cd11f4972b92c88c52624f7a4c5a96fd07347433",
  "csv_size_bytes": 26732653,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260913_015127Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210675,
  "items_db": 211516,
  "items_missing_in_db": 20,
  "codes_upstream": 86640,
  "codes_db": 255440,
  "codes_missing_in_db": 17,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 20,
  "db_inserted_codes": 17
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255477,
  "distinct_bl_part_id": 176376,
  "null_boid": 177300,
  "null_weight": 100195,
  "null_bk_part_id": 37,
  "null_bk_part_key": 37,
  "null_api_item_type": 37,
  "null_brikick_name": 37,
  "null_part_name": 101756,
  "null_element_id": 172240,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177300`
- null_weight: `100195`
- corruption_pattern_count: `0`
