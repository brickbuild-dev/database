# Brikick DB Post-Update Report

- created_at_utc: `20260318_011118Z`
- db_path: `database/brickovery.db`
- db_sha256: `183a5ea9d5527d5f9b108d5e27b886f82f215d7bee7aa8b193a9ca1b8eae2a2f`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260318_011107Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260318_011107Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "599c2e4a6f5389433aef87725a5a1dfd6ef9fcccd556f0d84ca233f4cb16e9bf",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260318_011107Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203672,
    "items_db": 203704,
    "items_missing_in_db": 42,
    "codes_upstream": 84011,
    "codes_db": 244077,
    "codes_missing_in_db": 16,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "3b5c963c64f1577cf28e175000eb5417faeb19c9a09c40af56c0290ab4f48733",
  "csv_size_bytes": 26082465,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260318_011107Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203672,
  "items_db": 203704,
  "items_missing_in_db": 42,
  "codes_upstream": 84011,
  "codes_db": 244077,
  "codes_missing_in_db": 16,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 42,
  "db_inserted_codes": 16
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 244135,
  "distinct_bl_part_id": 169453,
  "null_boid": 165968,
  "null_weight": 90309,
  "null_bk_part_id": 58,
  "null_bk_part_key": 58,
  "null_api_item_type": 58,
  "null_brikick_name": 58,
  "null_part_name": 90414,
  "null_element_id": 160898,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165968`
- null_weight: `90309`
- corruption_pattern_count: `0`
