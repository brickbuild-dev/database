# Brikick DB Post-Update Report

- created_at_utc: `20260807_020737Z`
- db_path: `database/brickovery.db`
- db_sha256: `0c2aedb1abf30be2999db43b448c180bd0fd5c8852921d1fe9f7ce5cdbf5dbbc`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260807_020726Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260807_020726Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "d26915eededa6ce59fef4e9823b221ccf0e4e79cb69a4617d6712860cc6a3e7f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260807_020726Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209261,
    "items_db": 210007,
    "items_missing_in_db": 28,
    "codes_upstream": 86028,
    "codes_db": 253248,
    "codes_missing_in_db": 13,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "69f71f141726de6b89b44d1fe40dee5f351f23c4fda43c8240a799be76169730",
  "csv_size_bytes": 26605330,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260807_020726Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209261,
  "items_db": 210007,
  "items_missing_in_db": 28,
  "codes_upstream": 86028,
  "codes_db": 253248,
  "codes_missing_in_db": 13,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 28,
  "db_inserted_codes": 13
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253289,
  "distinct_bl_part_id": 175087,
  "null_boid": 175112,
  "null_weight": 98097,
  "null_bk_part_id": 41,
  "null_bk_part_key": 41,
  "null_api_item_type": 41,
  "null_brikick_name": 41,
  "null_part_name": 99568,
  "null_element_id": 170052,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175112`
- null_weight: `98097`
- corruption_pattern_count: `0`
