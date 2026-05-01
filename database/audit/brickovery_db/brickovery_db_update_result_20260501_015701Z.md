# Brikick DB Post-Update Report

- created_at_utc: `20260501_015701Z`
- db_path: `database/brickovery.db`
- db_sha256: `4dbea653c996b87be297838c7df7f7466941b4fc054c87890ae76d32e6924202`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260501_015650Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260501_015650Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "4f87787b4815b04bf540d28cf1115a8a107c2144bc10e5a77d9cfffa306ef7b1",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260501_015650Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205393,
    "items_db": 205763,
    "items_missing_in_db": 4,
    "codes_upstream": 84464,
    "codes_db": 246598,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "66548c1f6cdd23ef54eb2241c2bdfa0ebb37174ebdaea494d13ca3fcacf7e48c",
  "csv_size_bytes": 26224555,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260501_015650Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205393,
  "items_db": 205763,
  "items_missing_in_db": 4,
  "codes_upstream": 84464,
  "codes_db": 246598,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 4,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246602,
  "distinct_bl_part_id": 171379,
  "null_boid": 168428,
  "null_weight": 92489,
  "null_bk_part_id": 4,
  "null_bk_part_key": 4,
  "null_api_item_type": 4,
  "null_brikick_name": 4,
  "null_part_name": 92881,
  "null_element_id": 163365,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168428`
- null_weight: `92489`
- corruption_pattern_count: `0`
