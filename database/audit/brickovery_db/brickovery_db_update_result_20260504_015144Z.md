# Brikick DB Post-Update Report

- created_at_utc: `20260504_015144Z`
- db_path: `database/brickovery.db`
- db_sha256: `6d238c78b588806ece6930ff6bdbd4587c02a743033e58081304e292122893da`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260504_015134Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260504_015134Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "c6c2cac68524776efaa2a2ee50415ac1b4b1b1e4e030e1500b9583733cf02e1e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260504_015134Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205650,
    "items_db": 205979,
    "items_missing_in_db": 69,
    "codes_upstream": 84733,
    "codes_db": 247036,
    "codes_missing_in_db": 59,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "e326ac5a53744cd3ad98accf4b2a926b1bbedd20996c3ba590e9b71f42877794",
  "csv_size_bytes": 26249998,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260504_015134Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205650,
  "items_db": 205979,
  "items_missing_in_db": 69,
  "codes_upstream": 84733,
  "codes_db": 247036,
  "codes_missing_in_db": 59,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 69,
  "db_inserted_codes": 59
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247164,
  "distinct_bl_part_id": 171596,
  "null_boid": 168990,
  "null_weight": 92875,
  "null_bk_part_id": 128,
  "null_bk_part_key": 128,
  "null_api_item_type": 128,
  "null_brikick_name": 128,
  "null_part_name": 93443,
  "null_element_id": 163927,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168990`
- null_weight: `92875`
- corruption_pattern_count: `0`
