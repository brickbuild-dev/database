# Brikick DB Post-Update Report

- created_at_utc: `20261106_040600Z`
- db_path: `database/brickovery.db`
- db_sha256: `aa00fb4595044809ada1ad85376ac3f430780c0db2ef31644f57a546f03b5f8f`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261106_040548Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261106_040548Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "0d3fe3d1c9f8117a7102073212b2508afbf63f7f34439953c6ffc8a5b794cb15",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261106_040548Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212087,
    "items_db": 213944,
    "items_missing_in_db": 23,
    "codes_upstream": 87174,
    "codes_db": 258763,
    "codes_missing_in_db": 25,
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
  "csv_sha256": "c83d98eac6af05b677d2e6110d9e43af2d69bc70ce80717a7bf409e545519c11",
  "csv_size_bytes": 26923513,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261106_040548Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212087,
  "items_db": 213944,
  "items_missing_in_db": 23,
  "codes_upstream": 87174,
  "codes_db": 258763,
  "codes_missing_in_db": 25,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 23,
  "db_inserted_codes": 23
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258809,
  "distinct_bl_part_id": 178670,
  "null_boid": 180629,
  "null_weight": 103363,
  "null_bk_part_id": 46,
  "null_bk_part_key": 46,
  "null_api_item_type": 46,
  "null_brikick_name": 46,
  "null_part_name": 105088,
  "null_element_id": 175572,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180629`
- null_weight: `103363`
- corruption_pattern_count: `0`
