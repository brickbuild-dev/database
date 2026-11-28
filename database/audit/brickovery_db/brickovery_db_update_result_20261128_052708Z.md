# Brikick DB Post-Update Report

- created_at_utc: `20261128_052708Z`
- db_path: `database/brickovery.db`
- db_sha256: `630065671ad362ca0d0e2576ab440db1b0fe3cc36cb43109c91bd0e8ca83a22d`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261128_052657Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261128_052657Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "65db880d4115543297dd795a3f4db85cc705c65eca041b9eee18d0d8c30ba286",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261128_052657Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212229,
    "items_db": 214103,
    "items_missing_in_db": 12,
    "codes_upstream": 87207,
    "codes_db": 258970,
    "codes_missing_in_db": 6,
    "unknown_color_tokens": [
      "Royal Blue",
      "Speckle Copper",
      "Speckle Gold",
      "Speckle Silver"
    ],
    "unknown_color_tokens_count": 4,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "5d204370b9853c408908e3aa201ea8b10a6d15f52c11be3ab948f127cdd36a88",
  "csv_size_bytes": 26935547,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261128_052657Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212229,
  "items_db": 214103,
  "items_missing_in_db": 12,
  "codes_upstream": 87207,
  "codes_db": 258970,
  "codes_missing_in_db": 6,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 12,
  "db_inserted_codes": 6
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258988,
  "distinct_bl_part_id": 178794,
  "null_boid": 180808,
  "null_weight": 103514,
  "null_bk_part_id": 18,
  "null_bk_part_key": 18,
  "null_api_item_type": 18,
  "null_brikick_name": 18,
  "null_part_name": 105267,
  "null_element_id": 175751,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180808`
- null_weight: `103514`
- corruption_pattern_count: `0`
