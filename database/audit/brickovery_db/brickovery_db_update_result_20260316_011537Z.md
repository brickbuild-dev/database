# Brikick DB Post-Update Report

- created_at_utc: `20260316_011537Z`
- db_path: `database/brickovery.db`
- db_sha256: `d9f580213977373a6e1884ab794a11def0d6e74c0fa363fce96341f1c0933dac`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260316_011525Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260316_011525Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "1e52b527efe388e9d199a7d359dbbedf4f7aa301b58e6a89362807da2d7ceac4",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260316_011525Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203585,
    "items_db": 203633,
    "items_missing_in_db": 23,
    "codes_upstream": 83964,
    "codes_db": 243974,
    "codes_missing_in_db": 4,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "0a88ac49ab4935bd842697846fec6b6ebf921fffbcf3550f9c6d517bbbec41fd",
  "csv_size_bytes": 26076563,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260316_011525Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203585,
  "items_db": 203633,
  "items_missing_in_db": 23,
  "codes_upstream": 83964,
  "codes_db": 243974,
  "codes_missing_in_db": 4,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 23,
  "db_inserted_codes": 4
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 244001,
  "distinct_bl_part_id": 169366,
  "null_boid": 165834,
  "null_weight": 90177,
  "null_bk_part_id": 27,
  "null_bk_part_key": 27,
  "null_api_item_type": 27,
  "null_brikick_name": 27,
  "null_part_name": 90280,
  "null_element_id": 160764,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165834`
- null_weight: `90177`
- corruption_pattern_count: `0`
