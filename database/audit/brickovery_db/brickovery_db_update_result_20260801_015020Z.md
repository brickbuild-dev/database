# Brikick DB Post-Update Report

- created_at_utc: `20260801_015020Z`
- db_path: `database/brickovery.db`
- db_sha256: `049fc912f0e3cd2db521500df6a5c9c1615c72f88a699add9f1bfc25014b6f60`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260801_015009Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260801_015009Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "5d64e2456fa8cbdcb290a7bc2a4978418df5db5aef27d0cfd04f16cbc7980848",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260801_015009Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 208649,
    "items_db": 208997,
    "items_missing_in_db": 386,
    "codes_upstream": 85793,
    "codes_db": 251972,
    "codes_missing_in_db": 52,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "5601e9d5372cff92191a5713e47ea23a07531b2c4f05ac63fd1880df738878c8",
  "csv_size_bytes": 26533529,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260801_015009Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 208649,
  "items_db": 208997,
  "items_missing_in_db": 386,
  "codes_upstream": 85793,
  "codes_db": 251972,
  "codes_missing_in_db": 52,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 386,
  "db_inserted_codes": 50
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 252408,
  "distinct_bl_part_id": 174599,
  "null_boid": 174231,
  "null_weight": 97285,
  "null_bk_part_id": 436,
  "null_bk_part_key": 436,
  "null_api_item_type": 436,
  "null_brikick_name": 436,
  "null_part_name": 98687,
  "null_element_id": 169171,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `174231`
- null_weight: `97285`
- corruption_pattern_count: `0`
