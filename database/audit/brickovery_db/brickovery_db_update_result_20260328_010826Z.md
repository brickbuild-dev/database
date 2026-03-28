# Brikick DB Post-Update Report

- created_at_utc: `20260328_010826Z`
- db_path: `database/brickovery.db`
- db_sha256: `e637827d068404b1d9054be9dc2965501477e73af09af3a4c99c9c9cf4b31f4c`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260328_010815Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260328_010815Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "ef6c5913639e5db2a55e6b21f616da8f966e449e04cb137b4904fd907432adb2",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260328_010815Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 204535,
    "items_db": 204611,
    "items_missing_in_db": 20,
    "codes_upstream": 84066,
    "codes_db": 245051,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "5127943b9900e3311783aa80223f314f405cd2657364b9fa8181822114ab8df0",
  "csv_size_bytes": 26135442,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260328_010815Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 204535,
  "items_db": 204611,
  "items_missing_in_db": 20,
  "codes_upstream": 84066,
  "codes_db": 245051,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 20,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 245071,
  "distinct_bl_part_id": 170329,
  "null_boid": 166901,
  "null_weight": 91224,
  "null_bk_part_id": 20,
  "null_bk_part_key": 20,
  "null_api_item_type": 20,
  "null_brikick_name": 20,
  "null_part_name": 91350,
  "null_element_id": 161834,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `166901`
- null_weight: `91224`
- corruption_pattern_count: `0`
