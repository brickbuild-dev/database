# Brikick DB Post-Update Report

- created_at_utc: `20260428_015203Z`
- db_path: `database/brickovery.db`
- db_sha256: `9f586e94d04d4b74be493fe4cb6dc0a52f18e72006912e8e40f3227808856508`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260428_015152Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260428_015152Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "415d13ba3ff1ece05953d719a85b3768e7c5d547c13d0f57a1bd73714172eeb0",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260428_015152Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205354,
    "items_db": 205726,
    "items_missing_in_db": 2,
    "codes_upstream": 84274,
    "codes_db": 246361,
    "codes_missing_in_db": 13,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "25be968780448fabc86bc8058b21590b8664bd7e605b4409af3d776fdea35ae3",
  "csv_size_bytes": 26210884,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260428_015152Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205354,
  "items_db": 205726,
  "items_missing_in_db": 2,
  "codes_upstream": 84274,
  "codes_db": 246361,
  "codes_missing_in_db": 13,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 2,
  "db_inserted_codes": 13
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246376,
  "distinct_bl_part_id": 171340,
  "null_boid": 168202,
  "null_weight": 92421,
  "null_bk_part_id": 15,
  "null_bk_part_key": 15,
  "null_api_item_type": 15,
  "null_brikick_name": 15,
  "null_part_name": 92655,
  "null_element_id": 163139,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168202`
- null_weight: `92421`
- corruption_pattern_count: `0`
