# Brikick DB Post-Update Report

- created_at_utc: `20260517_015923Z`
- db_path: `database/brickovery.db`
- db_sha256: `cf323b037f29b57b1eee8a71e8ed852dade3242773a7a660018599933d1e3ffa`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260517_015912Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260517_015912Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "adec1489ad39e7eeb00fd0a4145f7571800cbe7bb84076a2f59b9f7b5b7881aa",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260517_015912Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205860,
    "items_db": 206321,
    "items_missing_in_db": 13,
    "codes_upstream": 84369,
    "codes_db": 247898,
    "codes_missing_in_db": 2,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "8e617ec72c3086354cd8f980b486d31b4019ed01ae814f3ed82f95a7efa7c56b",
  "csv_size_bytes": 26300015,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260517_015912Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205860,
  "items_db": 206321,
  "items_missing_in_db": 13,
  "codes_upstream": 84369,
  "codes_db": 247898,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 13,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247913,
  "distinct_bl_part_id": 171865,
  "null_boid": 169738,
  "null_weight": 93359,
  "null_bk_part_id": 15,
  "null_bk_part_key": 15,
  "null_api_item_type": 15,
  "null_brikick_name": 15,
  "null_part_name": 94192,
  "null_element_id": 164676,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169738`
- null_weight: `93359`
- corruption_pattern_count: `0`
