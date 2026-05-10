# Brikick DB Post-Update Report

- created_at_utc: `20260510_015346Z`
- db_path: `database/brickovery.db`
- db_sha256: `2ce0cf15f60bc1c42b7786ac7012ac51cc1dad7633fa326a366deb510332d894`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260510_015334Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260510_015334Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "93bf9f918f2155fb4135413b705ac3ecf008d1579b7873f8e3f3f1d3d3024148",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260510_015334Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205741,
    "items_db": 206164,
    "items_missing_in_db": 23,
    "codes_upstream": 84225,
    "codes_db": 247592,
    "codes_missing_in_db": 22,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "dd1caebad39ef3bc3d6b2fe7176afed7b7a80da61278b570ee09d3142da7bd28",
  "csv_size_bytes": 26282207,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260510_015334Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205741,
  "items_db": 206164,
  "items_missing_in_db": 23,
  "codes_upstream": 84225,
  "codes_db": 247592,
  "codes_missing_in_db": 22,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 23,
  "db_inserted_codes": 21
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247636,
  "distinct_bl_part_id": 171723,
  "null_boid": 169462,
  "null_weight": 93135,
  "null_bk_part_id": 44,
  "null_bk_part_key": 44,
  "null_api_item_type": 44,
  "null_brikick_name": 44,
  "null_part_name": 93915,
  "null_element_id": 164399,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169462`
- null_weight: `93135`
- corruption_pattern_count: `0`
