# Brikick DB Post-Update Report

- created_at_utc: `20260625_021020Z`
- db_path: `database/brickovery.db`
- db_sha256: `d3fc7c1cc6078e57905c1c935379f8c24f4e73dfb07d0f270bcd829e11503e30`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260625_021009Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260625_021009Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "70e88340bfadbd7ec6a91dba607d1d808e9fd23d53f83700af0c2fde4e253f43",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260625_021009Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207450,
    "items_db": 208005,
    "items_missing_in_db": 104,
    "codes_upstream": 84965,
    "codes_db": 250177,
    "codes_missing_in_db": 40,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "dfa2568fda7e1745fa7059d3fe8d22246949619d02597400db4631b080a9ca4a",
  "csv_size_bytes": 26430831,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260625_021009Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207450,
  "items_db": 208005,
  "items_missing_in_db": 104,
  "codes_upstream": 84965,
  "codes_db": 250177,
  "codes_missing_in_db": 40,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 104,
  "db_inserted_codes": 36
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250317,
  "distinct_bl_part_id": 173357,
  "null_boid": 172141,
  "null_weight": 95648,
  "null_bk_part_id": 140,
  "null_bk_part_key": 140,
  "null_api_item_type": 140,
  "null_brikick_name": 140,
  "null_part_name": 96596,
  "null_element_id": 167080,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172141`
- null_weight: `95648`
- corruption_pattern_count: `0`
