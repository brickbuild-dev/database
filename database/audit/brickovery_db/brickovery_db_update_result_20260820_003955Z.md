# Brikick DB Post-Update Report

- created_at_utc: `20260820_003955Z`
- db_path: `database/brickovery.db`
- db_sha256: `025a7260141ed7571864058af575200947615e015f259fd4f52a4a164339aa1a`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260820_003944Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260820_003944Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "b158cea30766c9a8f4b29be9426c706419ccea38bd65f8571bf7ee7a1672514a",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260820_003944Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209674,
    "items_db": 210462,
    "items_missing_in_db": 2,
    "codes_upstream": 86234,
    "codes_db": 253947,
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
  "csv_sha256": "b6444d1d34e8b01b4595ff5814e158ef8ca952fa74d8d4272001d26dff701f6c",
  "csv_size_bytes": 26645784,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260820_003944Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209674,
  "items_db": 210462,
  "items_missing_in_db": 2,
  "codes_upstream": 86234,
  "codes_db": 253947,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 2,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253949,
  "distinct_bl_part_id": 175508,
  "null_boid": 175772,
  "null_weight": 98753,
  "null_bk_part_id": 2,
  "null_bk_part_key": 2,
  "null_api_item_type": 2,
  "null_brikick_name": 2,
  "null_part_name": 100228,
  "null_element_id": 170712,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175772`
- null_weight: `98753`
- corruption_pattern_count: `0`
