# Brikick DB Post-Update Report

- created_at_utc: `20260803_013535Z`
- db_path: `database/brickovery.db`
- db_sha256: `355029de057fd0e5a8bf451e611ca9c0bae8bef79fbad74b02d35a0b92d2ee76`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260803_013524Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260803_013524Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "5159affedb9e59e808a5b3c8d1ccca1d1bf6c8565a88e4b688b96beae0f8dfbe",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260803_013524Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209073,
    "items_db": 209802,
    "items_missing_in_db": 34,
    "codes_upstream": 85983,
    "codes_db": 252946,
    "codes_missing_in_db": 53,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "8f073746c3efabeb83be99350dca6ebd8cf7d879a1dedd3ee01c409e9573fca7",
  "csv_size_bytes": 26588460,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260803_013524Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209073,
  "items_db": 209802,
  "items_missing_in_db": 34,
  "codes_upstream": 85983,
  "codes_db": 252946,
  "codes_missing_in_db": 53,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 34,
  "db_inserted_codes": 53
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253033,
  "distinct_bl_part_id": 174889,
  "null_boid": 174856,
  "null_weight": 97878,
  "null_bk_part_id": 87,
  "null_bk_part_key": 87,
  "null_api_item_type": 87,
  "null_brikick_name": 87,
  "null_part_name": 99312,
  "null_element_id": 169796,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `174856`
- null_weight: `97878`
- corruption_pattern_count: `0`
