# Brikick DB Post-Update Report

- created_at_utc: `20260809_005053Z`
- db_path: `database/brickovery.db`
- db_sha256: `05b05f3c2d3a8408a05a9cec2c7bdabfcfdf3d450a8032561d1b97b304b3b7cb`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260809_005046Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260809_005046Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "b5a72873f1f2fc98984522d607352cabfa2df2fd1c8b0d51f32b44943bec5df4",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260809_005046Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209329,
    "items_db": 210082,
    "items_missing_in_db": 21,
    "codes_upstream": 86014,
    "codes_db": 253354,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "c7177173afb75e5ebffa8a29de0f3919815564861e98bd6bbed27c6335db364b",
  "csv_size_bytes": 26611484,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260809_005046Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209329,
  "items_db": 210082,
  "items_missing_in_db": 21,
  "codes_upstream": 86014,
  "codes_db": 253354,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 21,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253375,
  "distinct_bl_part_id": 175155,
  "null_boid": 175198,
  "null_weight": 98183,
  "null_bk_part_id": 21,
  "null_bk_part_key": 21,
  "null_api_item_type": 21,
  "null_brikick_name": 21,
  "null_part_name": 99654,
  "null_element_id": 170138,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175198`
- null_weight: `98183`
- corruption_pattern_count: `0`
