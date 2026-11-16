# Brikick DB Post-Update Report

- created_at_utc: `20261116_033934Z`
- db_path: `database/brickovery.db`
- db_sha256: `638a69a1fee481f03182f1523317e30a74df2d1ef85e4983116f8ffbd3ea9eae`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261116_033925Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261116_033925Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "2ea63a3123aeb4bd4af2d5471f56c51917157b18a2f4d1f99881c7c39044cd91",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261116_033925Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212125,
    "items_db": 213994,
    "items_missing_in_db": 12,
    "codes_upstream": 87183,
    "codes_db": 258843,
    "codes_missing_in_db": 1,
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
  "csv_sha256": "2eb7e2d186b9f6c3588ab1b378fc6bb52d91f92ca557be75628d25509e98b6f3",
  "csv_size_bytes": 26928147,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261116_033925Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212125,
  "items_db": 213994,
  "items_missing_in_db": 12,
  "codes_upstream": 87183,
  "codes_db": 258843,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 12,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258856,
  "distinct_bl_part_id": 178707,
  "null_boid": 180676,
  "null_weight": 103382,
  "null_bk_part_id": 13,
  "null_bk_part_key": 13,
  "null_api_item_type": 13,
  "null_brikick_name": 13,
  "null_part_name": 105135,
  "null_element_id": 175619,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180676`
- null_weight: `103382`
- corruption_pattern_count: `0`
