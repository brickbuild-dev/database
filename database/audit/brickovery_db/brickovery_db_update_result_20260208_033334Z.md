# Brikick DB Post-Update Report

- created_at_utc: `20260208_033334Z`
- db_path: `database/brickovery.db`
- db_sha256: `790167fb7a884a79ffe2e84bf5733249898ec7b896f989847ae8fe1eb59024b5`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260208_033323Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260208_033323Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "32023d95569a0bdef03ead750e472abbe7863f34186f22daf7edbe0024bd36c8",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260208_033323Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202428,
    "items_db": 202422,
    "items_missing_in_db": 8,
    "codes_upstream": 83295,
    "codes_db": 242127,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "7859de4b02af76d11943f8f8d5a054be9f916573b473c7d1e6118bd8f0b5ce52",
  "csv_size_bytes": 25970355,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260208_033323Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202428,
  "items_db": 202422,
  "items_missing_in_db": 8,
  "codes_upstream": 83295,
  "codes_db": 242127,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 8,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242135,
  "distinct_bl_part_id": 168285,
  "null_boid": 163969,
  "null_weight": 88659,
  "null_bk_part_id": 8,
  "null_bk_part_key": 8,
  "null_api_item_type": 8,
  "null_brikick_name": 8,
  "null_part_name": 88414,
  "null_element_id": 158898,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `163969`
- null_weight: `88659`
- corruption_pattern_count: `0`
