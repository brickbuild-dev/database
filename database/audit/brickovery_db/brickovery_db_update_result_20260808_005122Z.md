# Brikick DB Post-Update Report

- created_at_utc: `20260808_005122Z`
- db_path: `database/brickovery.db`
- db_sha256: `ec9204bc772e626b2b7d95dbb36e89fcb3b1803173df4b3b30ca5cf7b788861c`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260808_005111Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260808_005111Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "555903df2bb8438721911be64c39845f7fda3549ac363974050b6b71e9673185",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260808_005111Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209308,
    "items_db": 210035,
    "items_missing_in_db": 47,
    "codes_upstream": 86012,
    "codes_db": 253289,
    "codes_missing_in_db": 19,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "237546fcb127427a4126945dcd967907f72ecd398ee15d16fe6ec283a1c06e65",
  "csv_size_bytes": 26607736,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260808_005111Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209308,
  "items_db": 210035,
  "items_missing_in_db": 47,
  "codes_upstream": 86012,
  "codes_db": 253289,
  "codes_missing_in_db": 19,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 47,
  "db_inserted_codes": 18
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253354,
  "distinct_bl_part_id": 175134,
  "null_boid": 175177,
  "null_weight": 98162,
  "null_bk_part_id": 65,
  "null_bk_part_key": 65,
  "null_api_item_type": 65,
  "null_brikick_name": 65,
  "null_part_name": 99633,
  "null_element_id": 170117,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175177`
- null_weight: `98162`
- corruption_pattern_count: `0`
