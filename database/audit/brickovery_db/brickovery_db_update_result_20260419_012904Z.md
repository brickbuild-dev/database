# Brikick DB Post-Update Report

- created_at_utc: `20260419_012904Z`
- db_path: `database/brickovery.db`
- db_sha256: `1998feb3c36cf9809444d8989ae85e27905f279f1d61f04db0d7c2a146d28b22`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260419_012852Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260419_012852Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "ebc44f2ce5826116442c5cc50ea8a86e0037f50717e1a42936f1b342f7c8f294",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260419_012852Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205238,
    "items_db": 205578,
    "items_missing_in_db": 15,
    "codes_upstream": 84162,
    "codes_db": 246103,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "4bae95c571cd645542a85b004b77642de6e2f5cd735e9937413a435c696c0f7c",
  "csv_size_bytes": 26196059,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260419_012852Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205238,
  "items_db": 205578,
  "items_missing_in_db": 15,
  "codes_upstream": 84162,
  "codes_db": 246103,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 15,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246118,
  "distinct_bl_part_id": 171232,
  "null_boid": 167948,
  "null_weight": 92249,
  "null_bk_part_id": 15,
  "null_bk_part_key": 15,
  "null_api_item_type": 15,
  "null_brikick_name": 15,
  "null_part_name": 92397,
  "null_element_id": 162881,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167948`
- null_weight: `92249`
- corruption_pattern_count: `0`
