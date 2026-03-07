# Brikick DB Post-Update Report

- created_at_utc: `20260307_010213Z`
- db_path: `database/brickovery.db`
- db_sha256: `ce5fb12806e1391033b368806069246dd7e90fb50f2a67e152a41aaed4383ec5`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260307_010202Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260307_010202Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "9c1c926aaa8c545309e59701b6cec672b6763d2a8845e019c3b7a4c88b1eb08b",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260307_010202Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203348,
    "items_db": 203377,
    "items_missing_in_db": 25,
    "codes_upstream": 83833,
    "codes_db": 243576,
    "codes_missing_in_db": 27,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "d29622351d314e140cd6363cc531b859b929f3185e37f619f27aa496a61d8f6e",
  "csv_size_bytes": 26053615,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260307_010202Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203348,
  "items_db": 203377,
  "items_missing_in_db": 25,
  "codes_upstream": 83833,
  "codes_db": 243576,
  "codes_missing_in_db": 27,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 25,
  "db_inserted_codes": 27
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243628,
  "distinct_bl_part_id": 169118,
  "null_boid": 165461,
  "null_weight": 89822,
  "null_bk_part_id": 52,
  "null_bk_part_key": 52,
  "null_api_item_type": 52,
  "null_brikick_name": 52,
  "null_part_name": 89907,
  "null_element_id": 160391,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165461`
- null_weight: `89822`
- corruption_pattern_count: `0`
