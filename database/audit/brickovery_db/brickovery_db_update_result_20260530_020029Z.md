# Brikick DB Post-Update Report

- created_at_utc: `20260530_020029Z`
- db_path: `database/brickovery.db`
- db_sha256: `da733a6cb91446aade85ad4427f63fb6a98cf2952dc5d97b97f562afa6ad232a`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260530_020017Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260530_020017Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "33e4e570a556bdb815ce8b3f7011daa07a06a249bebc2010c18c8c605c02109a",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260530_020017Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205999,
    "items_db": 206532,
    "items_missing_in_db": 46,
    "codes_upstream": 84410,
    "codes_db": 248206,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "776bde7a58ef15d6b91ec4b01463d5530c8165bbdfbd08bbd68d6f7be8b8f66e",
  "csv_size_bytes": 26317459,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260530_020017Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205999,
  "items_db": 206532,
  "items_missing_in_db": 46,
  "codes_upstream": 84410,
  "codes_db": 248206,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 46,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248252,
  "distinct_bl_part_id": 172090,
  "null_boid": 170077,
  "null_weight": 93689,
  "null_bk_part_id": 46,
  "null_bk_part_key": 46,
  "null_api_item_type": 46,
  "null_brikick_name": 46,
  "null_part_name": 94531,
  "null_element_id": 165015,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `170077`
- null_weight: `93689`
- corruption_pattern_count: `0`
