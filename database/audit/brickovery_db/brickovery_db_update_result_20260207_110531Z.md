# Brikick DB Post-Update Report

- created_at_utc: `20260207_110531Z`
- db_path: `database/brickovery.db`
- db_sha256: `5fc6d7d2da765d73c311f17e3f75b4ee2a7691cc9c5d119f6b494214467ed1a6`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260207_110521Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260207_110521Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "d7ec1ce52fd15db31afcc891c76ef5908113bb3ece27740e5c85ea96dd92143c",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260207_110521Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202414,
    "items_db": 202414,
    "items_missing_in_db": 2,
    "codes_upstream": 83290,
    "codes_db": 242114,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "bb1360415428dd116d31abf9fde255b163bcbc2178b9344b2e7948bc1564b6c6",
  "csv_size_bytes": 25969602,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260207_110521Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202414,
  "items_db": 202414,
  "items_missing_in_db": 2,
  "codes_upstream": 83290,
  "codes_db": 242114,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 2,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242116,
  "distinct_bl_part_id": 168271,
  "null_boid": 163950,
  "null_weight": 88640,
  "null_bk_part_id": 2,
  "null_bk_part_key": 2,
  "null_api_item_type": 2,
  "null_brikick_name": 2,
  "null_part_name": 88395,
  "null_element_id": 158879,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `163950`
- null_weight: `88640`
- corruption_pattern_count: `0`
