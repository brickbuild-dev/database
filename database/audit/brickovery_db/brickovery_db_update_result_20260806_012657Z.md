# Brikick DB Post-Update Report

- created_at_utc: `20260806_012657Z`
- db_path: `database/brickovery.db`
- db_sha256: `55ff3b040c7220930f4179f591947fd76025ebb318a1ac27654540996f92a4a6`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260806_012645Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260806_012645Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "5312ba3ad4c6018e74bfe23c76faf6cca724c778759e7592541cdad129e57107",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260806_012645Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209234,
    "items_db": 209890,
    "items_missing_in_db": 117,
    "codes_upstream": 86015,
    "codes_db": 253126,
    "codes_missing_in_db": 5,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "d726024741967185eea40e5dc6845967403e23cc935e356ffdef5eead7e2ee2b",
  "csv_size_bytes": 26598709,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260806_012645Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209234,
  "items_db": 209890,
  "items_missing_in_db": 117,
  "codes_upstream": 86015,
  "codes_db": 253126,
  "codes_missing_in_db": 5,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 117,
  "db_inserted_codes": 5
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253248,
  "distinct_bl_part_id": 175059,
  "null_boid": 175071,
  "null_weight": 98056,
  "null_bk_part_id": 122,
  "null_bk_part_key": 122,
  "null_api_item_type": 122,
  "null_brikick_name": 122,
  "null_part_name": 99527,
  "null_element_id": 170011,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175071`
- null_weight: `98056`
- corruption_pattern_count: `0`
