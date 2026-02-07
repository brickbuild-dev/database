# Brikick DB Post-Update Report

- created_at_utc: `20260207_150007Z`
- db_path: `database/brickovery.db`
- db_sha256: `9ed1b5976c8b4013183d93b3594b03451dde1bb5cd035a8f145bd0ac3caafbca`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260207_145956Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260207_145956Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "f7f4c1768b32bfe012b5167dbe672532f0cd10de93c53285f6e4368138ff226d",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260207_145956Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202415,
    "items_db": 202416,
    "items_missing_in_db": 1,
    "codes_upstream": 83290,
    "codes_db": 242116,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "bdd293819ee1bee37c7ae9abf3667fca8128c5a98d9ac3a64e410a158a9e56b1",
  "csv_size_bytes": 25969708,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260207_145956Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202415,
  "items_db": 202416,
  "items_missing_in_db": 1,
  "codes_upstream": 83290,
  "codes_db": 242116,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 1,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242117,
  "distinct_bl_part_id": 168272,
  "null_boid": 163951,
  "null_weight": 88641,
  "null_bk_part_id": 1,
  "null_bk_part_key": 1,
  "null_api_item_type": 1,
  "null_brikick_name": 1,
  "null_part_name": 88396,
  "null_element_id": 158880,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `163951`
- null_weight: `88641`
- corruption_pattern_count: `0`
