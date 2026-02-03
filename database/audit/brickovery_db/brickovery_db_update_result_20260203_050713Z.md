# Brikick DB Post-Update Report

- created_at_utc: `20260203_050713Z`
- db_path: `database/brickovery.db`
- db_sha256: `f08aa9f1ac8b5c3947d9d5695025f59e0293e1e05a53c11e5173ecd887a5df1b`
- db_size_bytes: `88244224`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260203_050703Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260203_050703Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "eeae1c531a19d0ccfa16ccc26b71df589285dbb8b2dfe7d7b785e8661cf02e23",
  "db_size_bytes": 88240128,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260203_050703Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202386,
    "items_db": 237909,
    "items_missing_in_db": 18,
    "codes_upstream": 83275,
    "codes_db": 282541,
    "codes_missing_in_db": 2,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "e37e78e570442922a4ab580a6a3051e71e25851eb0139f1af3012f20d64f91d7",
  "csv_size_bytes": 16838071,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260203_050703Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202386,
  "items_db": 237909,
  "items_missing_in_db": 18,
  "codes_upstream": 83275,
  "codes_db": 282541,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 18,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 4,
  "brickovery_db_rows": 282561,
  "distinct_bl_part_id": 203783,
  "null_boid": 168403,
  "null_weight": 109202,
  "null_bk_part_id": 20,
  "null_bk_part_key": 20,
  "null_api_item_type": 20,
  "null_brikick_name": 20,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168403`
- null_weight: `109202`
- corruption_pattern_count: `0`
