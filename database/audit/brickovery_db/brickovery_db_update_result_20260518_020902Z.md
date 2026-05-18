# Brikick DB Post-Update Report

- created_at_utc: `20260518_020902Z`
- db_path: `database/brickovery.db`
- db_sha256: `1cf6fc5a63a37a24b80af36d689d300d31dc94f179723de47c6279a608724912`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260518_020850Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260518_020850Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "5180b9e450394075cb67b1d507402dfb41ac5fb6f62c8373b3a93fe475e40a4a",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260518_020850Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205869,
    "items_db": 206334,
    "items_missing_in_db": 23,
    "codes_upstream": 84370,
    "codes_db": 247913,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "1c80b881eedf7401a4d80d15d4feaa9dac1ea5fa88921a8e5cc5c31af54cab54",
  "csv_size_bytes": 26300833,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260518_020850Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205869,
  "items_db": 206334,
  "items_missing_in_db": 23,
  "codes_upstream": 84370,
  "codes_db": 247913,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 23,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247936,
  "distinct_bl_part_id": 171885,
  "null_boid": 169761,
  "null_weight": 93382,
  "null_bk_part_id": 23,
  "null_bk_part_key": 23,
  "null_api_item_type": 23,
  "null_brikick_name": 23,
  "null_part_name": 94215,
  "null_element_id": 164699,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169761`
- null_weight: `93382`
- corruption_pattern_count: `0`
