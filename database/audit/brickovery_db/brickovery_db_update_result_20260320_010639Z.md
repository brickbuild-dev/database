# Brikick DB Post-Update Report

- created_at_utc: `20260320_010639Z`
- db_path: `database/brickovery.db`
- db_sha256: `b23e45de29fd0e52df65b8dc915fbefdc4ba515f553fbd8f8209fbc272103975`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260320_010628Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260320_010628Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "09b7d11d2860f552f029ff747161e0c56e8ca74ce7e7cddff6c5a226fb62b226",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260320_010628Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203699,
    "items_db": 203768,
    "items_missing_in_db": 7,
    "codes_upstream": 84031,
    "codes_db": 244157,
    "codes_missing_in_db": 18,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "128bbd37a8d7be8c62dfd7dcc0c7a70d723017d0f2a298e4d7feda27bb94b9d3",
  "csv_size_bytes": 26087034,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260320_010628Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203699,
  "items_db": 203768,
  "items_missing_in_db": 7,
  "codes_upstream": 84031,
  "codes_db": 244157,
  "codes_missing_in_db": 18,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 7,
  "db_inserted_codes": 18
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 244182,
  "distinct_bl_part_id": 169482,
  "null_boid": 166015,
  "null_weight": 90356,
  "null_bk_part_id": 25,
  "null_bk_part_key": 25,
  "null_api_item_type": 25,
  "null_brikick_name": 25,
  "null_part_name": 90461,
  "null_element_id": 160945,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `166015`
- null_weight: `90356`
- corruption_pattern_count: `0`
