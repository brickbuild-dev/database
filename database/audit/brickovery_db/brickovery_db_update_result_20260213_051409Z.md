# Brikick DB Post-Update Report

- created_at_utc: `20260213_051409Z`
- db_path: `database/brickovery.db`
- db_sha256: `afeff72e011b3bf7500bf1bb3099a9849c527b583dc2001c7c82bd16d65ee331`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260213_051358Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260213_051358Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "890e8b23392499ecf2b27144df606553e9e74f9b48160b66c5576017f280907e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260213_051358Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202469,
    "items_db": 202464,
    "items_missing_in_db": 9,
    "codes_upstream": 83315,
    "codes_db": 242186,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "2d27c94466274c9b88c9dca57219c8b15e4489f387c0981ca28589599569a0d4",
  "csv_size_bytes": 25973821,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260213_051358Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202469,
  "items_db": 202464,
  "items_missing_in_db": 9,
  "codes_upstream": 83315,
  "codes_db": 242186,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 9,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242195,
  "distinct_bl_part_id": 168322,
  "null_boid": 164028,
  "null_weight": 88718,
  "null_bk_part_id": 9,
  "null_bk_part_key": 9,
  "null_api_item_type": 9,
  "null_brikick_name": 9,
  "null_part_name": 88474,
  "null_element_id": 158958,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `164028`
- null_weight: `88718`
- corruption_pattern_count: `0`
