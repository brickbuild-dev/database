# Brikick DB Post-Update Report

- created_at_utc: `20260805_012948Z`
- db_path: `database/brickovery.db`
- db_sha256: `9427f8ab5effc40ad4541bd750675f819dbe5eecc5b88aae334e3af14941bade`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260805_012936Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260805_012936Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "c37b4619e2c89dc522ca3f13b85fb86060f287f19bb4bbb516b163c79d3219fe",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260805_012936Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209117,
    "items_db": 209861,
    "items_missing_in_db": 29,
    "codes_upstream": 86010,
    "codes_db": 253079,
    "codes_missing_in_db": 20,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "dea86bbfaa4ae8bf6c52ec97ba6c6c5f5e507226d4dfd838d445d85aa4d59d75",
  "csv_size_bytes": 26596022,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260805_012936Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209117,
  "items_db": 209861,
  "items_missing_in_db": 29,
  "codes_upstream": 86010,
  "codes_db": 253079,
  "codes_missing_in_db": 20,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 29,
  "db_inserted_codes": 18
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253126,
  "distinct_bl_part_id": 174942,
  "null_boid": 174949,
  "null_weight": 97934,
  "null_bk_part_id": 47,
  "null_bk_part_key": 47,
  "null_api_item_type": 47,
  "null_brikick_name": 47,
  "null_part_name": 99405,
  "null_element_id": 169889,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `174949`
- null_weight: `97934`
- corruption_pattern_count: `0`
