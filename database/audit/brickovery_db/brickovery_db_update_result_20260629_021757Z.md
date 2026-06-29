# Brikick DB Post-Update Report

- created_at_utc: `20260629_021757Z`
- db_path: `database/brickovery.db`
- db_sha256: `add1ac13eb9ca83fdfe6ea8f65731426cd65df6cf7d33b7b9be4865a31175f5b`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260629_021747Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260629_021747Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "cbac16c20209e1b5c6b5da0ecf35336e94cf054ac2888f1b7f8ecee6c2f26781",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260629_021747Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207547,
    "items_db": 208207,
    "items_missing_in_db": 14,
    "codes_upstream": 85071,
    "codes_db": 250509,
    "codes_missing_in_db": 10,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "cccc78fc17f3be4bcdf7f6d6d7225bd865cee42b0c93c7713a27a951c67947e9",
  "csv_size_bytes": 26450242,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260629_021747Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207547,
  "items_db": 208207,
  "items_missing_in_db": 14,
  "codes_upstream": 85071,
  "codes_db": 250509,
  "codes_missing_in_db": 10,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 14,
  "db_inserted_codes": 10
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250533,
  "distinct_bl_part_id": 173468,
  "null_boid": 172357,
  "null_weight": 95852,
  "null_bk_part_id": 24,
  "null_bk_part_key": 24,
  "null_api_item_type": 24,
  "null_brikick_name": 24,
  "null_part_name": 96812,
  "null_element_id": 167296,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172357`
- null_weight: `95852`
- corruption_pattern_count: `0`
