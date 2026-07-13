# Brikick DB Post-Update Report

- created_at_utc: `20260713_013340Z`
- db_path: `database/brickovery.db`
- db_sha256: `98676cacd9ab8158005f8033497e5a8707194c0a3289d66610592a7acb9497ed`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260713_013328Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260713_013328Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "d4bebba4ae8d3379f4c3532047363a2035b30e21b6343fe10bad1f482067c274",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260713_013328Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207842,
    "items_db": 208507,
    "items_missing_in_db": 24,
    "codes_upstream": 85355,
    "codes_db": 251031,
    "codes_missing_in_db": 73,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "58214ddc319942abee51ddb09e7551a126af0c4b9ece526624c0dde8c233c95b",
  "csv_size_bytes": 26480511,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260713_013328Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207842,
  "items_db": 208507,
  "items_missing_in_db": 24,
  "codes_upstream": 85355,
  "codes_db": 251031,
  "codes_missing_in_db": 73,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 24,
  "db_inserted_codes": 73
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251128,
  "distinct_bl_part_id": 173751,
  "null_boid": 172952,
  "null_weight": 96367,
  "null_bk_part_id": 97,
  "null_bk_part_key": 97,
  "null_api_item_type": 97,
  "null_brikick_name": 97,
  "null_part_name": 97407,
  "null_element_id": 167891,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172952`
- null_weight: `96367`
- corruption_pattern_count: `0`
