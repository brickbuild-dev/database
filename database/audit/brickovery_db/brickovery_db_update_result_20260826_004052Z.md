# Brikick DB Post-Update Report

- created_at_utc: `20260826_004052Z`
- db_path: `database/brickovery.db`
- db_sha256: `05a6e0a3ac1643e16b86f6d21624ed2fc3a44fc2c7c7d155c16e6674af7fd6d7`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260826_004040Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260826_004040Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "a692cc0756cdb9507e536567031bc6fead8f7593f3ddcfcc675b4f4f76d17e65",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260826_004040Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209840,
    "items_db": 210625,
    "items_missing_in_db": 25,
    "codes_upstream": 86341,
    "codes_db": 254207,
    "codes_missing_in_db": 22,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "9eefe2eae1dd2ed982a533925a73cd5990ed0f1412673e0d8a1319ffaa651c42",
  "csv_size_bytes": 26660969,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260826_004040Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209840,
  "items_db": 210625,
  "items_missing_in_db": 25,
  "codes_upstream": 86341,
  "codes_db": 254207,
  "codes_missing_in_db": 22,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 25,
  "db_inserted_codes": 21
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254253,
  "distinct_bl_part_id": 175694,
  "null_boid": 176076,
  "null_weight": 99052,
  "null_bk_part_id": 46,
  "null_bk_part_key": 46,
  "null_api_item_type": 46,
  "null_brikick_name": 46,
  "null_part_name": 100532,
  "null_element_id": 171016,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176076`
- null_weight: `99052`
- corruption_pattern_count: `0`
