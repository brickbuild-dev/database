# Brikick DB Post-Update Report

- created_at_utc: `20260217_051613Z`
- db_path: `database/brickovery.db`
- db_sha256: `03b57bb5eef582ffa85271d72cd1c56d1534d622066eb2d42d48b66bcaa15b6d`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260217_051602Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260217_051602Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "380241427a44ddf55614b9e474f375eda92645f484d91df7fa20db1e9dde4622",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260217_051602Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202522,
    "items_db": 202500,
    "items_missing_in_db": 29,
    "codes_upstream": 83430,
    "codes_db": 242242,
    "codes_missing_in_db": 93,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "050dae0a4e7c9d80fcd90e3185aae1cb4b58e46ced18eb044eff6fdf3449d06f",
  "csv_size_bytes": 25977068,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260217_051602Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202522,
  "items_db": 202500,
  "items_missing_in_db": 29,
  "codes_upstream": 83430,
  "codes_db": 242242,
  "codes_missing_in_db": 93,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 29,
  "db_inserted_codes": 93
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242364,
  "distinct_bl_part_id": 168371,
  "null_boid": 164197,
  "null_weight": 88871,
  "null_bk_part_id": 122,
  "null_bk_part_key": 122,
  "null_api_item_type": 122,
  "null_brikick_name": 122,
  "null_part_name": 88643,
  "null_element_id": 159127,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `164197`
- null_weight: `88871`
- corruption_pattern_count: `0`
