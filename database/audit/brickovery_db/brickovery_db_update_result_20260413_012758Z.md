# Brikick DB Post-Update Report

- created_at_utc: `20260413_012758Z`
- db_path: `database/brickovery.db`
- db_sha256: `1577ca733ab0c828a30a505101412315da0677ea8ef4ac35fde1527cfa6c57f7`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260413_012746Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260413_012746Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "25fb541c9e35100928cb1aefcd2140ac7d65afcbb0759877b8eeebbf45406412",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260413_012746Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205183,
    "items_db": 205524,
    "items_missing_in_db": 7,
    "codes_upstream": 84145,
    "codes_db": 246032,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "8c6a3c91fdf0b1e7c589731f40b247a475fb43fcf23f584bcdaf1c420f6ae80f",
  "csv_size_bytes": 26191974,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260413_012746Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205183,
  "items_db": 205524,
  "items_missing_in_db": 7,
  "codes_upstream": 84145,
  "codes_db": 246032,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 7,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246039,
  "distinct_bl_part_id": 171177,
  "null_boid": 167869,
  "null_weight": 92177,
  "null_bk_part_id": 7,
  "null_bk_part_key": 7,
  "null_api_item_type": 7,
  "null_brikick_name": 7,
  "null_part_name": 92318,
  "null_element_id": 162802,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167869`
- null_weight: `92177`
- corruption_pattern_count: `0`
