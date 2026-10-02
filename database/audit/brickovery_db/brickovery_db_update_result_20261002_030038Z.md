# Brikick DB Post-Update Report

- created_at_utc: `20261002_030038Z`
- db_path: `database/brickovery.db`
- db_sha256: `053b29c0bf33bb7204147ebd14dffbf182a00e056efc39d04f38e3a7f6b81011`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261002_030026Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261002_030026Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "e7c5dad136dcebd8710e2e2ae74c29c89f43dbe12c1b8eb342038e4d46764d87",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261002_030026Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211385,
    "items_db": 213135,
    "items_missing_in_db": 86,
    "codes_upstream": 86746,
    "codes_db": 257548,
    "codes_missing_in_db": 8,
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
  "csv_sha256": "519a54b116378c72525c578bbfe0714d8500f6d4c1c7a14e3b31d02e24579a9b",
  "csv_size_bytes": 26853336,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261002_030026Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211385,
  "items_db": 213135,
  "items_missing_in_db": 86,
  "codes_upstream": 86746,
  "codes_db": 257548,
  "codes_missing_in_db": 8,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 86,
  "db_inserted_codes": 8
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 257642,
  "distinct_bl_part_id": 177972,
  "null_boid": 179463,
  "null_weight": 102318,
  "null_bk_part_id": 94,
  "null_bk_part_key": 94,
  "null_api_item_type": 94,
  "null_brikick_name": 94,
  "null_part_name": 103921,
  "null_element_id": 174405,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179463`
- null_weight: `102318`
- corruption_pattern_count: `0`
