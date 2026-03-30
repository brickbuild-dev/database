# Brikick DB Post-Update Report

- created_at_utc: `20260330_011831Z`
- db_path: `database/brickovery.db`
- db_sha256: `b63be81363d7886f00e98fbe42a695dddaad9380a1bfda1204f8328d3a2d8ecd`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260330_011820Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260330_011820Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "214a4793b841719f725bb45c04632dd3bc7fdf5e1e97fbb074372b48cd35d8c8",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260330_011820Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 204583,
    "items_db": 204859,
    "items_missing_in_db": 49,
    "codes_upstream": 84069,
    "codes_db": 245299,
    "codes_missing_in_db": 3,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "4ff2adfddedbac1d2986f4e4afb9d3e85167374db9b41891dd828c5d4d841e7d",
  "csv_size_bytes": 26150246,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260330_011820Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 204583,
  "items_db": 204859,
  "items_missing_in_db": 49,
  "codes_upstream": 84069,
  "codes_db": 245299,
  "codes_missing_in_db": 3,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 49,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 245350,
  "distinct_bl_part_id": 170599,
  "null_boid": 167180,
  "null_weight": 91503,
  "null_bk_part_id": 51,
  "null_bk_part_key": 51,
  "null_api_item_type": 51,
  "null_brikick_name": 51,
  "null_part_name": 91629,
  "null_element_id": 162113,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167180`
- null_weight: `91503`
- corruption_pattern_count: `0`
