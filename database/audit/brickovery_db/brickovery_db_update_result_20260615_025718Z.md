# Brikick DB Post-Update Report

- created_at_utc: `20260615_025718Z`
- db_path: `database/brickovery.db`
- db_sha256: `b46e9dc12c2ac4cf3bc8f4e3887cdda90ff847f24a9f2d3baadd580796fc1424`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260615_025707Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260615_025707Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "3a504463e63866990e41b06cbe8af6f337edcb3e34f0c03ed47d246a28566217",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260615_025707Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207146,
    "items_db": 207757,
    "items_missing_in_db": 0,
    "codes_upstream": 84790,
    "codes_db": 249778,
    "codes_missing_in_db": 2,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "9cc1a246e3d46d684e90cce3348953959d7cf740455f3fc9ddbd0709d7761b41",
  "csv_size_bytes": 26407638,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260615_025707Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207146,
  "items_db": 207757,
  "items_missing_in_db": 0,
  "codes_upstream": 84790,
  "codes_db": 249778,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 0,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 249780,
  "distinct_bl_part_id": 173016,
  "null_boid": 171604,
  "null_weight": 95120,
  "null_bk_part_id": 2,
  "null_bk_part_key": 2,
  "null_api_item_type": 2,
  "null_brikick_name": 2,
  "null_part_name": 96059,
  "null_element_id": 166543,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171604`
- null_weight: `95120`
- corruption_pattern_count: `0`
