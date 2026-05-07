# Brikick DB Post-Update Report

- created_at_utc: `20260507_015411Z`
- db_path: `database/brickovery.db`
- db_sha256: `131a38e897a7f8b731198c22609360add8e84ddf9c6a5682f2622144b87a150b`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260507_015400Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260507_015400Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "07cce64c1b3b3250ed54565f14c75f8348b0c874fe649608d40cfb931db7a2bd",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260507_015400Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205691,
    "items_db": 206089,
    "items_missing_in_db": 38,
    "codes_upstream": 84953,
    "codes_db": 247388,
    "codes_missing_in_db": 91,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "7d6fc03a67292134540980504338ab2c431e15954d37a7f7a6716f28833c90a0",
  "csv_size_bytes": 26270304,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260507_015400Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205691,
  "items_db": 206089,
  "items_missing_in_db": 38,
  "codes_upstream": 84953,
  "codes_db": 247388,
  "codes_missing_in_db": 91,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 38,
  "db_inserted_codes": 87
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247513,
  "distinct_bl_part_id": 171672,
  "null_boid": 169339,
  "null_weight": 93090,
  "null_bk_part_id": 125,
  "null_bk_part_key": 125,
  "null_api_item_type": 125,
  "null_brikick_name": 125,
  "null_part_name": 93792,
  "null_element_id": 164276,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169339`
- null_weight: `93090`
- corruption_pattern_count: `0`
