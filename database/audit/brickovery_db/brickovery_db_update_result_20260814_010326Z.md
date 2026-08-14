# Brikick DB Post-Update Report

- created_at_utc: `20260814_010326Z`
- db_path: `database/brickovery.db`
- db_sha256: `258067aff5d63c28c72ae3cf83c42e69f54dbf8a153b5b8bc5aa0442fbe77d9a`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260814_010314Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260814_010314Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "c3a8d2038a017521acb843d6d855063660cb367e70c83b062c2e4fb7f9fd67ef",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260814_010314Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209557,
    "items_db": 210334,
    "items_missing_in_db": 3,
    "codes_upstream": 86145,
    "codes_db": 253716,
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
  "csv_sha256": "84c60cd528e8b02e100a94fb1e6e9072406cae49eff3dc844c936518065821e9",
  "csv_size_bytes": 26632323,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260814_010314Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209557,
  "items_db": 210334,
  "items_missing_in_db": 3,
  "codes_upstream": 86145,
  "codes_db": 253716,
  "codes_missing_in_db": 18,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 3,
  "db_inserted_codes": 15
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253734,
  "distinct_bl_part_id": 175385,
  "null_boid": 175557,
  "null_weight": 98540,
  "null_bk_part_id": 18,
  "null_bk_part_key": 18,
  "null_api_item_type": 18,
  "null_brikick_name": 18,
  "null_part_name": 100013,
  "null_element_id": 170497,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175557`
- null_weight: `98540`
- corruption_pattern_count: `0`
