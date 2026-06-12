# Brikick DB Post-Update Report

- created_at_utc: `20260612_021912Z`
- db_path: `database/brickovery.db`
- db_sha256: `7f951028e739ed8e2213b5f4c4453fa71c1f94838fd85d7a7e8d95e3008791f4`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260612_021900Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260612_021900Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "68483ee53027460acdba204d00918dfe4f1f7552c95c0438eb36397415356855",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260612_021900Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 206729,
    "items_db": 207309,
    "items_missing_in_db": 20,
    "codes_upstream": 84679,
    "codes_db": 249214,
    "codes_missing_in_db": 13,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "c813b870969dd6cec1f3c16ffe6dc81d706f2c7316eb9e4d578409302a39f467",
  "csv_size_bytes": 26376080,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260612_021900Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 206729,
  "items_db": 207309,
  "items_missing_in_db": 20,
  "codes_upstream": 84679,
  "codes_db": 249214,
  "codes_missing_in_db": 13,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 20,
  "db_inserted_codes": 13
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 249247,
  "distinct_bl_part_id": 172589,
  "null_boid": 171072,
  "null_weight": 94601,
  "null_bk_part_id": 33,
  "null_bk_part_key": 33,
  "null_api_item_type": 33,
  "null_brikick_name": 33,
  "null_part_name": 95526,
  "null_element_id": 166010,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171072`
- null_weight: `94601`
- corruption_pattern_count: `0`
