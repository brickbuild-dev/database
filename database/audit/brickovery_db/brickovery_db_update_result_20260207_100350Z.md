# Brikick DB Post-Update Report

- created_at_utc: `20260207_100350Z`
- db_path: `database/brickovery.db`
- db_sha256: `cb6d8196eea7b8e0426ae7ff57e1e8fcd0c547c92a92ab34763bd3fc5bd90a9b`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260207_100339Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260207_100339Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "8711aecd187e6e820032a93605fbbc536e603936edf7254c78164866cbac84b1",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260207_100339Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202412,
    "items_db": 202411,
    "items_missing_in_db": 3,
    "codes_upstream": 83290,
    "codes_db": 242111,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "65273b5f98f213d3437f5ced0f1a311996d5392fcf1e22ef414905a3cc0dbe70",
  "csv_size_bytes": 25969448,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260207_100339Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202412,
  "items_db": 202411,
  "items_missing_in_db": 3,
  "codes_upstream": 83290,
  "codes_db": 242111,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 3,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242114,
  "distinct_bl_part_id": 168269,
  "null_boid": 163948,
  "null_weight": 88638,
  "null_bk_part_id": 3,
  "null_bk_part_key": 3,
  "null_api_item_type": 3,
  "null_brikick_name": 3,
  "null_part_name": 88393,
  "null_element_id": 158877,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `163948`
- null_weight: `88638`
- corruption_pattern_count: `0`
