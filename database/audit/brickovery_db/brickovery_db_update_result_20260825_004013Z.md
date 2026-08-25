# Brikick DB Post-Update Report

- created_at_utc: `20260825_004013Z`
- db_path: `database/brickovery.db`
- db_sha256: `90dd9ecf2286cc4305365879baebbf176ac999bb5d6e2445c4533e75983a840b`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260825_004002Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260825_004002Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "458bceb8943c0e37f2001a4a020a7422df370706126bccba38d054593dc1242e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260825_004002Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209827,
    "items_db": 210587,
    "items_missing_in_db": 38,
    "codes_upstream": 86329,
    "codes_db": 254154,
    "codes_missing_in_db": 18,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "0f64114bb0a70a6693dc8cfc62e87a2d98df6d8af9165de4c1abf26b04a30f40",
  "csv_size_bytes": 26657916,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260825_004002Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209827,
  "items_db": 210587,
  "items_missing_in_db": 38,
  "codes_upstream": 86329,
  "codes_db": 254154,
  "codes_missing_in_db": 18,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 38,
  "db_inserted_codes": 15
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254207,
  "distinct_bl_part_id": 175669,
  "null_boid": 176030,
  "null_weight": 99006,
  "null_bk_part_id": 53,
  "null_bk_part_key": 53,
  "null_api_item_type": 53,
  "null_brikick_name": 53,
  "null_part_name": 100486,
  "null_element_id": 170970,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176030`
- null_weight: `99006`
- corruption_pattern_count: `0`
