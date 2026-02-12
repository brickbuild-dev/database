# Brikick DB Post-Update Report

- created_at_utc: `20260212_051902Z`
- db_path: `database/brickovery.db`
- db_sha256: `297377ca7f6a3bd8fe90719775d615e5c56f5fe00640c2c7ac73a296970a2439`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260212_051851Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260212_051851Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "71d5c3716330e97e7e4cc2a2e08e012340024b77a7c0e19abcbc8a32c66d7bd1",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260212_051851Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202460,
    "items_db": 202458,
    "items_missing_in_db": 5,
    "codes_upstream": 83312,
    "codes_db": 242179,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "c1fd62ac444df8c3b74680cc211619aac0f2672be77cd82c5e8fb594c2db4f58",
  "csv_size_bytes": 25973411,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260212_051851Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202460,
  "items_db": 202458,
  "items_missing_in_db": 5,
  "codes_upstream": 83312,
  "codes_db": 242179,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 5,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242185,
  "distinct_bl_part_id": 168314,
  "null_boid": 164018,
  "null_weight": 88708,
  "null_bk_part_id": 6,
  "null_bk_part_key": 6,
  "null_api_item_type": 6,
  "null_brikick_name": 6,
  "null_part_name": 88464,
  "null_element_id": 158948,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `164018`
- null_weight: `88708`
- corruption_pattern_count: `0`
