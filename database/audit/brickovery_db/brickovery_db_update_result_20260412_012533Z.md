# Brikick DB Post-Update Report

- created_at_utc: `20260412_012533Z`
- db_path: `database/brickovery.db`
- db_sha256: `7048dd6bb0340c77403dcce0ff21250480abbd5c16ebad88ada454f87d6d24b8`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260412_012522Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260412_012522Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "7c080f2f76844952900b61d978c9a776bb1fa6c866a5f7f8bf6e057852220dcb",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260412_012522Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205178,
    "items_db": 205510,
    "items_missing_in_db": 14,
    "codes_upstream": 84144,
    "codes_db": 246014,
    "codes_missing_in_db": 6,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "532580589d2447f60a9c755e42e92d3829569fad57f14f6fd734f75187c16dec",
  "csv_size_bytes": 26190973,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260412_012522Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205178,
  "items_db": 205510,
  "items_missing_in_db": 14,
  "codes_upstream": 84144,
  "codes_db": 246014,
  "codes_missing_in_db": 6,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 14,
  "db_inserted_codes": 4
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246032,
  "distinct_bl_part_id": 171170,
  "null_boid": 167862,
  "null_weight": 92171,
  "null_bk_part_id": 18,
  "null_bk_part_key": 18,
  "null_api_item_type": 18,
  "null_brikick_name": 18,
  "null_part_name": 92311,
  "null_element_id": 162795,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167862`
- null_weight: `92171`
- corruption_pattern_count: `0`
