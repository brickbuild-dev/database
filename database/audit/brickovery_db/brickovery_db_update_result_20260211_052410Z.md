# Brikick DB Post-Update Report

- created_at_utc: `20260211_052410Z`
- db_path: `database/brickovery.db`
- db_sha256: `95b34c8044f869d8d39239e32ac63fd0d617d35025a654c69c72dc431ed9dee0`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260211_052359Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260211_052359Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "2f3546a5b7c2429036396ef6ee72f929b2b107488706ff661c49459dda8b7fc2",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260211_052359Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202455,
    "items_db": 202447,
    "items_missing_in_db": 11,
    "codes_upstream": 83311,
    "codes_db": 242162,
    "codes_missing_in_db": 6,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "446aac8703f5ec4498fee3cee229cef396417177d782a9db2a66abaf5aff79f8",
  "csv_size_bytes": 25972422,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260211_052359Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202455,
  "items_db": 202447,
  "items_missing_in_db": 11,
  "codes_upstream": 83311,
  "codes_db": 242162,
  "codes_missing_in_db": 6,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 11,
  "db_inserted_codes": 6
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242179,
  "distinct_bl_part_id": 168309,
  "null_boid": 164012,
  "null_weight": 88703,
  "null_bk_part_id": 17,
  "null_bk_part_key": 17,
  "null_api_item_type": 17,
  "null_brikick_name": 17,
  "null_part_name": 88458,
  "null_element_id": 158942,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `164012`
- null_weight: `88703`
- corruption_pattern_count: `0`
