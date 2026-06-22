# Brikick DB Post-Update Report

- created_at_utc: `20260622_024123Z`
- db_path: `database/brickovery.db`
- db_sha256: `1f5f05528d54cbaae3c5e97462f3bda62b962b8b7fd0390bed599cf421fafb89`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260622_024112Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260622_024112Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "7f1fedb735b597d3d651680abe87583f7f234b5e47a1f8957891ddb2a41e05d0",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260622_024112Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207349,
    "items_db": 207977,
    "items_missing_in_db": 6,
    "codes_upstream": 84937,
    "codes_db": 250135,
    "codes_missing_in_db": 2,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "c36cffd18521010d7408421f7eb0ff14e3f34a9df0a65bcc904a719912dfdfc4",
  "csv_size_bytes": 26428385,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260622_024112Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207349,
  "items_db": 207977,
  "items_missing_in_db": 6,
  "codes_upstream": 84937,
  "codes_db": 250135,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 6,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250142,
  "distinct_bl_part_id": 173236,
  "null_boid": 171966,
  "null_weight": 95476,
  "null_bk_part_id": 7,
  "null_bk_part_key": 7,
  "null_api_item_type": 7,
  "null_brikick_name": 7,
  "null_part_name": 96421,
  "null_element_id": 166905,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171966`
- null_weight: `95476`
- corruption_pattern_count: `0`
