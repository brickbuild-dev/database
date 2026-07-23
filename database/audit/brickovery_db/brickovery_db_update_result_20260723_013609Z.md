# Brikick DB Post-Update Report

- created_at_utc: `20260723_013609Z`
- db_path: `database/brickovery.db`
- db_sha256: `48988512504dc23cfcaab907003bbaf52e11d9c2d97ae9ffef7fd452ade305e6`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260723_013557Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260723_013557Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "2513770f8c9ab3df466445ab30144bc20432655abe0e4c1e6c9d3710f92baec3",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260723_013557Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 208047,
    "items_db": 208741,
    "items_missing_in_db": 10,
    "codes_upstream": 85405,
    "codes_db": 251380,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "b7f85f139479476f8c231df051c371f4eeb5e8f75de38c77a7d31a053b5b5cf8",
  "csv_size_bytes": 26500334,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260723_013557Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 208047,
  "items_db": 208741,
  "items_missing_in_db": 10,
  "codes_upstream": 85405,
  "codes_db": 251380,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 10,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251390,
  "distinct_bl_part_id": 173967,
  "null_boid": 173214,
  "null_weight": 96561,
  "null_bk_part_id": 10,
  "null_bk_part_key": 10,
  "null_api_item_type": 10,
  "null_brikick_name": 10,
  "null_part_name": 97669,
  "null_element_id": 168153,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `173214`
- null_weight: `96561`
- corruption_pattern_count: `0`
