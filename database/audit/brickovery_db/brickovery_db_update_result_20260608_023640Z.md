# Brikick DB Post-Update Report

- created_at_utc: `20260608_023640Z`
- db_path: `database/brickovery.db`
- db_sha256: `d936014d67201db781ae007b8db888ade35be5304ea9d9d86624f5543f103719`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260608_023629Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260608_023629Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "04da2017bab8683e574e96213ceef91ca9bb1aeeee2a500e84302acfc04e8c9f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260608_023629Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 206636,
    "items_db": 207203,
    "items_missing_in_db": 29,
    "codes_upstream": 84569,
    "codes_db": 248976,
    "codes_missing_in_db": 47,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "d1a77b865c84409065a40ce64592843b8a014da8245a0a4b8efdd85277350adb",
  "csv_size_bytes": 26362436,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260608_023629Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 206636,
  "items_db": 207203,
  "items_missing_in_db": 29,
  "codes_upstream": 84569,
  "codes_db": 248976,
  "codes_missing_in_db": 47,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 29,
  "db_inserted_codes": 46
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 249051,
  "distinct_bl_part_id": 172493,
  "null_boid": 170876,
  "null_weight": 94462,
  "null_bk_part_id": 75,
  "null_bk_part_key": 75,
  "null_api_item_type": 75,
  "null_brikick_name": 75,
  "null_part_name": 95330,
  "null_element_id": 165814,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `170876`
- null_weight: `94462`
- corruption_pattern_count: `0`
