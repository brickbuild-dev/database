# Brikick DB Post-Update Report

- created_at_utc: `20260818_003857Z`
- db_path: `database/brickovery.db`
- db_sha256: `7e557f0916e23e0be38f2f7871c93b9e9f10629e5e4ec74b76f07697ae810f85`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260818_003845Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260818_003845Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "c720707de4eaca7a66b5b7f81cc9ddafc1457c1500e9bd9841ab0562f3a042c4",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260818_003845Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209670,
    "items_db": 210453,
    "items_missing_in_db": 4,
    "codes_upstream": 86234,
    "codes_db": 253935,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "f9ccac8e3a7a3d140fa1518327dc8f852a49dad83ca946866e26ded24fc224bf",
  "csv_size_bytes": 26645096,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260818_003845Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209670,
  "items_db": 210453,
  "items_missing_in_db": 4,
  "codes_upstream": 86234,
  "codes_db": 253935,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 4,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253939,
  "distinct_bl_part_id": 175502,
  "null_boid": 175762,
  "null_weight": 98743,
  "null_bk_part_id": 4,
  "null_bk_part_key": 4,
  "null_api_item_type": 4,
  "null_brikick_name": 4,
  "null_part_name": 100218,
  "null_element_id": 170702,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175762`
- null_weight: `98743`
- corruption_pattern_count: `0`
