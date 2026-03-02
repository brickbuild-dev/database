# Brikick DB Post-Update Report

- created_at_utc: `20260302_010540Z`
- db_path: `database/brickovery.db`
- db_sha256: `d536fc490457ad208836b8f82d614602545531d49fe3978a3f48bbfdcff07c97`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260302_010529Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260302_010529Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "9421804b3ae5dc3992a30d1907e5c22338d67a55fe4f99bee859f3fc4b56b08f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260302_010529Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203221,
    "items_db": 203045,
    "items_missing_in_db": 223,
    "codes_upstream": 83725,
    "codes_db": 243105,
    "codes_missing_in_db": 71,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "2cced9334fef0473c61d2c41bbc4da15581459c56a6c0a856d4213625a3c6661",
  "csv_size_bytes": 26025908,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260302_010529Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203221,
  "items_db": 203045,
  "items_missing_in_db": 223,
  "codes_upstream": 83725,
  "codes_db": 243105,
  "codes_missing_in_db": 71,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 223,
  "db_inserted_codes": 65
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243393,
  "distinct_bl_part_id": 168984,
  "null_boid": 165226,
  "null_weight": 89606,
  "null_bk_part_id": 288,
  "null_bk_part_key": 288,
  "null_api_item_type": 288,
  "null_brikick_name": 288,
  "null_part_name": 89672,
  "null_element_id": 160156,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165226`
- null_weight: `89606`
- corruption_pattern_count: `0`
