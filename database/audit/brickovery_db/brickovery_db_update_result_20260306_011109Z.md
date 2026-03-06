# Brikick DB Post-Update Report

- created_at_utc: `20260306_011109Z`
- db_path: `database/brickovery.db`
- db_sha256: `2a1e809df9572102f1f97b1fc4354482f66e53686a2a61032102390b52986559`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260306_011058Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260306_011058Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "f457c8efb1cd3b212fd5a2831bde640d03071721dfe7100f75705c317f29de50",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260306_011058Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203324,
    "items_db": 203361,
    "items_missing_in_db": 16,
    "codes_upstream": 83807,
    "codes_db": 243550,
    "codes_missing_in_db": 10,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "3393f1e8bf25ebf3e3cc26dddbbb396a666b9786cd835b1d4027a0faa4dd86e8",
  "csv_size_bytes": 26052099,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260306_011058Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203324,
  "items_db": 203361,
  "items_missing_in_db": 16,
  "codes_upstream": 83807,
  "codes_db": 243550,
  "codes_missing_in_db": 10,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 16,
  "db_inserted_codes": 10
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243576,
  "distinct_bl_part_id": 169093,
  "null_boid": 165409,
  "null_weight": 89772,
  "null_bk_part_id": 26,
  "null_bk_part_key": 26,
  "null_api_item_type": 26,
  "null_brikick_name": 26,
  "null_part_name": 89855,
  "null_element_id": 160339,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165409`
- null_weight: `89772`
- corruption_pattern_count: `0`
