# Brikick DB Post-Update Report

- created_at_utc: `20260304_010410Z`
- db_path: `database/brickovery.db`
- db_sha256: `fe28465446ae2ad65dbc9f9dadad6c0d65d6e7d68c2440ede3776a487955942e`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260304_010359Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260304_010359Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "75b65e896befc54f9efd3ddca4b12da8b6bc701fc5ab8a283fdaa8f445e80e96",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260304_010359Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203291,
    "items_db": 203326,
    "items_missing_in_db": 15,
    "codes_upstream": 83779,
    "codes_db": 243482,
    "codes_missing_in_db": 20,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "cfb8ba9738a43cddd05163b5039f3aee29ef502e00a52af75a9a19370cb82ddd",
  "csv_size_bytes": 26048216,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260304_010359Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203291,
  "items_db": 203326,
  "items_missing_in_db": 15,
  "codes_upstream": 83779,
  "codes_db": 243482,
  "codes_missing_in_db": 20,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 15,
  "db_inserted_codes": 20
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243517,
  "distinct_bl_part_id": 169057,
  "null_boid": 165350,
  "null_weight": 89726,
  "null_bk_part_id": 35,
  "null_bk_part_key": 35,
  "null_api_item_type": 35,
  "null_brikick_name": 35,
  "null_part_name": 89796,
  "null_element_id": 160280,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165350`
- null_weight: `89726`
- corruption_pattern_count: `0`
