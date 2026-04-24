# Brikick DB Post-Update Report

- created_at_utc: `20260424_012907Z`
- db_path: `database/brickovery.db`
- db_sha256: `3befd846d4fa559abfd43c245aa04a09e8aaa756099d8b618b6869c9970e7609`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260424_012856Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260424_012856Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "a4cef9876f6fb5f2a82d347677428f4a03c007cdeba0249ba6cfe8b046233ebd",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260424_012856Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205282,
    "items_db": 205646,
    "items_missing_in_db": 3,
    "codes_upstream": 84246,
    "codes_db": 246194,
    "codes_missing_in_db": 75,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "467a08a55f3b794eaa69ad795a1fbf2250d4806d4eb164bd1026eed8676dee61",
  "csv_size_bytes": 26201234,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260424_012856Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205282,
  "items_db": 205646,
  "items_missing_in_db": 3,
  "codes_upstream": 84246,
  "codes_db": 246194,
  "codes_missing_in_db": 75,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 3,
  "db_inserted_codes": 75
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246272,
  "distinct_bl_part_id": 171282,
  "null_boid": 168098,
  "null_weight": 92402,
  "null_bk_part_id": 78,
  "null_bk_part_key": 78,
  "null_api_item_type": 78,
  "null_brikick_name": 78,
  "null_part_name": 92551,
  "null_element_id": 163035,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168098`
- null_weight: `92402`
- corruption_pattern_count: `0`
