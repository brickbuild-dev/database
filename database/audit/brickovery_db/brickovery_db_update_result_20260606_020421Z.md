# Brikick DB Post-Update Report

- created_at_utc: `20260606_020421Z`
- db_path: `database/brickovery.db`
- db_sha256: `c1d9ccc522d055b81f991078ea8f372ea6de8bfd9f0d22e6ef54abf6c3cd48e0`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260606_020410Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260606_020410Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "6a2ed8fc375dc6ad7b67b1e3c07c5c5d75ce085d64689a6699755e74a852c401",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260606_020410Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 206563,
    "items_db": 207148,
    "items_missing_in_db": 9,
    "codes_upstream": 84478,
    "codes_db": 248874,
    "codes_missing_in_db": 9,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "9954aa58ea6a1dff14fcb8e046831497a79bd9197c6ba98a1933eee4b7136da1",
  "csv_size_bytes": 26356588,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260606_020410Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 206563,
  "items_db": 207148,
  "items_missing_in_db": 9,
  "codes_upstream": 84478,
  "codes_db": 248874,
  "codes_missing_in_db": 9,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 9,
  "db_inserted_codes": 7
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248890,
  "distinct_bl_part_id": 172420,
  "null_boid": 170715,
  "null_weight": 94318,
  "null_bk_part_id": 16,
  "null_bk_part_key": 16,
  "null_api_item_type": 16,
  "null_brikick_name": 16,
  "null_part_name": 95169,
  "null_element_id": 165653,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `170715`
- null_weight: `94318`
- corruption_pattern_count: `0`
