# Brikick DB Post-Update Report

- created_at_utc: `20260721_013040Z`
- db_path: `database/brickovery.db`
- db_sha256: `ca34e716ae8f051f78402864be8de9ca2635372c395baa74f44351f177e0956e`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260721_013028Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260721_013028Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "e3c3810a5947a749c31b886bdee024881130eeaeaa35dce51ef7ecaf6fa76f3a",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260721_013028Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 208019,
    "items_db": 208588,
    "items_missing_in_db": 131,
    "codes_upstream": 85403,
    "codes_db": 251195,
    "codes_missing_in_db": 31,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "ed0f9f37515369a85e122ffab0bf948d4993c1e84798c0de7bd2322fbc86fb6c",
  "csv_size_bytes": 26489933,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260721_013028Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 208019,
  "items_db": 208588,
  "items_missing_in_db": 131,
  "codes_upstream": 85403,
  "codes_db": 251195,
  "codes_missing_in_db": 31,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 131,
  "db_inserted_codes": 31
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251357,
  "distinct_bl_part_id": 173936,
  "null_boid": 173181,
  "null_weight": 96528,
  "null_bk_part_id": 162,
  "null_bk_part_key": 162,
  "null_api_item_type": 162,
  "null_brikick_name": 162,
  "null_part_name": 97636,
  "null_element_id": 168120,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `173181`
- null_weight: `96528`
- corruption_pattern_count: `0`
