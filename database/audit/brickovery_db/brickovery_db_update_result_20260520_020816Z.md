# Brikick DB Post-Update Report

- created_at_utc: `20260520_020816Z`
- db_path: `database/brickovery.db`
- db_sha256: `183eb295a67daf39c9b13cc4c2de629a6484d4ddc9a16af194020bbc84aeaa54`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260520_020804Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260520_020804Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "ee168845603b8fbec7fb0fe9286053866b91bc8e2d21921b73bf3dc3ad57bd2f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260520_020804Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205887,
    "items_db": 206373,
    "items_missing_in_db": 24,
    "codes_upstream": 84386,
    "codes_db": 247957,
    "codes_missing_in_db": 6,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "74807ff939c90db84506b75fba8524d2d9c03ae3613e28fc793f90081e8a0300",
  "csv_size_bytes": 26303252,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260520_020804Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205887,
  "items_db": 206373,
  "items_missing_in_db": 24,
  "codes_upstream": 84386,
  "codes_db": 247957,
  "codes_missing_in_db": 6,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 24,
  "db_inserted_codes": 6
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247987,
  "distinct_bl_part_id": 171923,
  "null_boid": 169812,
  "null_weight": 93430,
  "null_bk_part_id": 30,
  "null_bk_part_key": 30,
  "null_api_item_type": 30,
  "null_brikick_name": 30,
  "null_part_name": 94266,
  "null_element_id": 164750,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169812`
- null_weight: `93430`
- corruption_pattern_count: `0`
