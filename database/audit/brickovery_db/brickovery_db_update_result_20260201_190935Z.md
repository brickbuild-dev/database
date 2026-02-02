# Brikick DB Post-Update Report

- created_at_utc: `20260201_190935Z`
- db_path: `database/brickovery.db`
- db_sha256: `024e477a4316d6396f5298b7fb7f5a34e1449f2f90cdeeab5f8108a52f3f6089`
- db_size_bytes: `44699648`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260201_190926Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260201_190926Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "7b20b49edf2a69995c282d5afdbcdc256096dc5d5188712e425fc8ab656405b6",
  "db_size_bytes": 44695552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260201_190926Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202369,
    "items_db": 237874,
    "items_missing_in_db": 35,
    "codes_upstream": 83273,
    "codes_db": 282504,
    "codes_missing_in_db": 2,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "e519823982e9812a2da4f913935a101697269d6e3ccd2e8319b44cfaea3568d6",
  "csv_size_bytes": 16155986,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260201_190926Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202369,
  "items_db": 237874,
  "items_missing_in_db": 35,
  "codes_upstream": 83273,
  "codes_db": 282504,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 35,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 4,
  "brickovery_db_rows": 282541,
  "distinct_bl_part_id": 203765,
  "null_boid": 282057,
  "null_weight": 109186,
  "null_bk_part_id": 37,
  "null_bk_part_key": 37,
  "null_api_item_type": 37,
  "null_brikick_name": 37,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `282057`
- null_weight: `109186`
- corruption_pattern_count: `0`
