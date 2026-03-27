# Brikick DB Post-Update Report

- created_at_utc: `20260327_011441Z`
- db_path: `database/brickovery.db`
- db_sha256: `b7f9766ec4e5d5731ac69cb0b27bacdb01abe3d4b77a168997a4cf61e1158fd4`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260327_011430Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260327_011430Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "3a4be55a68e319f757f39e9c1c2830e8ca31a0f92d71a416fd6dfcb529024d2f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260327_011430Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 204517,
    "items_db": 204204,
    "items_missing_in_db": 407,
    "codes_upstream": 84066,
    "codes_db": 244632,
    "codes_missing_in_db": 12,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "0a32a92bef7a435d0f5a32a6d9b93c8650824255fcb17b14823da7013ba08818",
  "csv_size_bytes": 26112536,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260327_011430Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 204517,
  "items_db": 204204,
  "items_missing_in_db": 407,
  "codes_upstream": 84066,
  "codes_db": 244632,
  "codes_missing_in_db": 12,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 407,
  "db_inserted_codes": 12
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 245051,
  "distinct_bl_part_id": 170309,
  "null_boid": 166883,
  "null_weight": 91212,
  "null_bk_part_id": 419,
  "null_bk_part_key": 419,
  "null_api_item_type": 419,
  "null_brikick_name": 419,
  "null_part_name": 91330,
  "null_element_id": 161814,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `166883`
- null_weight: `91212`
- corruption_pattern_count: `0`
