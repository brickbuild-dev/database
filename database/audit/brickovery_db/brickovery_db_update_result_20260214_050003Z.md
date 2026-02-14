# Brikick DB Post-Update Report

- created_at_utc: `20260214_050003Z`
- db_path: `database/brickovery.db`
- db_sha256: `393a24613dbc7208051a04e93e557426fdc203d29ba762afd905bc1e4fb42423`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260214_045953Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260214_045953Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "72acd4c21934d5708dd79e25795e68a91944f4bd1cf8a1c840e9a1c9f199c624",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260214_045953Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202476,
    "items_db": 202473,
    "items_missing_in_db": 7,
    "codes_upstream": 83320,
    "codes_db": 242195,
    "codes_missing_in_db": 5,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "08ddddcab11a276eb1dcaeb84c9593e56931e6672e0e45e896cfb3f6a0f94f0e",
  "csv_size_bytes": 25974308,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260214_045953Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202476,
  "items_db": 202473,
  "items_missing_in_db": 7,
  "codes_upstream": 83320,
  "codes_db": 242195,
  "codes_missing_in_db": 5,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 7,
  "db_inserted_codes": 3
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242205,
  "distinct_bl_part_id": 168329,
  "null_boid": 164038,
  "null_weight": 88728,
  "null_bk_part_id": 10,
  "null_bk_part_key": 10,
  "null_api_item_type": 10,
  "null_brikick_name": 10,
  "null_part_name": 88484,
  "null_element_id": 158968,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `164038`
- null_weight: `88728`
- corruption_pattern_count: `0`
