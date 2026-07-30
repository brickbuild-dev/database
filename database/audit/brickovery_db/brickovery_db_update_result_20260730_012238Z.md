# Brikick DB Post-Update Report

- created_at_utc: `20260730_012238Z`
- db_path: `database/brickovery.db`
- db_sha256: `b39183257d7bd671527162674a33d4bac6a7ad893996b7c82610878757ebfb30`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260730_012227Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260730_012227Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "badcb84b2a40361c1236335c3f27162f097b465eeae80b638f15cdfc9f11ab59",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260730_012227Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 208186,
    "items_db": 208861,
    "items_missing_in_db": 52,
    "codes_upstream": 85418,
    "codes_db": 251511,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "bcac021a7d79c768e8664a039b902890674b59bdc442fc106076f25ac53d431a",
  "csv_size_bytes": 26507318,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260730_012227Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 208186,
  "items_db": 208861,
  "items_missing_in_db": 52,
  "codes_upstream": 85418,
  "codes_db": 251511,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 52,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251563,
  "distinct_bl_part_id": 174129,
  "null_boid": 173387,
  "null_weight": 96726,
  "null_bk_part_id": 52,
  "null_bk_part_key": 52,
  "null_api_item_type": 52,
  "null_brikick_name": 52,
  "null_part_name": 97842,
  "null_element_id": 168326,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `173387`
- null_weight: `96726`
- corruption_pattern_count: `0`
