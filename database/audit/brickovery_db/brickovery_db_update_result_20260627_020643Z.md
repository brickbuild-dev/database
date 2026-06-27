# Brikick DB Post-Update Report

- created_at_utc: `20260627_020643Z`
- db_path: `database/brickovery.db`
- db_sha256: `c2e5c121444b0cf40fa21971895ce66f8d9eb0e7992a3cc88bc70bcbaeb10880`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260627_020632Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260627_020632Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "9e28b3f56c018fbb7f78c287504a569b1c6a6cd0a5596627df75007e8d25e545",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260627_020632Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207532,
    "items_db": 208182,
    "items_missing_in_db": 21,
    "codes_upstream": 85058,
    "codes_db": 250450,
    "codes_missing_in_db": 31,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "cc32fa97df5c489e12b3355edc8372b9b036a72b1f5c6e3df0d6465e383ba41a",
  "csv_size_bytes": 26446770,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260627_020632Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207532,
  "items_db": 208182,
  "items_missing_in_db": 21,
  "codes_upstream": 85058,
  "codes_db": 250450,
  "codes_missing_in_db": 31,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 21,
  "db_inserted_codes": 31
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250502,
  "distinct_bl_part_id": 173450,
  "null_boid": 172326,
  "null_weight": 95829,
  "null_bk_part_id": 52,
  "null_bk_part_key": 52,
  "null_api_item_type": 52,
  "null_brikick_name": 52,
  "null_part_name": 96781,
  "null_element_id": 167265,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172326`
- null_weight: `95829`
- corruption_pattern_count: `0`
