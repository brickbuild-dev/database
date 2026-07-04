# Brikick DB Post-Update Report

- created_at_utc: `20260704_015241Z`
- db_path: `database/brickovery.db`
- db_sha256: `80cbaff8279adec2fb4890f66983eb0ded1b96fd16281a6fce6f6d8d5ee4ec7c`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260704_015229Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260704_015229Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "e3073b203a73b579ed070c6b2e4767cfcc9dc2f7e5b29921af9847594e88b6da",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260704_015229Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207702,
    "items_db": 208325,
    "items_missing_in_db": 55,
    "codes_upstream": 85194,
    "codes_db": 250729,
    "codes_missing_in_db": 30,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "d790af51da4bdec6a7284d944637e5bbc668038e3bafabb38dcdba5f8c4613a1",
  "csv_size_bytes": 26462960,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260704_015229Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207702,
  "items_db": 208325,
  "items_missing_in_db": 55,
  "codes_upstream": 85194,
  "codes_db": 250729,
  "codes_missing_in_db": 30,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 55,
  "db_inserted_codes": 29
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250813,
  "distinct_bl_part_id": 173606,
  "null_boid": 172637,
  "null_weight": 96087,
  "null_bk_part_id": 84,
  "null_bk_part_key": 84,
  "null_api_item_type": 84,
  "null_brikick_name": 84,
  "null_part_name": 97092,
  "null_element_id": 167576,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172637`
- null_weight: `96087`
- corruption_pattern_count: `0`
