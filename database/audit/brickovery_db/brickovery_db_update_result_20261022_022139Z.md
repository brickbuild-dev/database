# Brikick DB Post-Update Report

- created_at_utc: `20261022_022139Z`
- db_path: `database/brickovery.db`
- db_sha256: `0fda207fa1af311551f7b2244411e3a30864e1a9815270d940c94a26e698a1ef`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261022_022127Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261022_022127Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "261e2a3e5531b4f5f7138463619c7bc39a8778fdf8cd9b8d9e23063f74e9aac8",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261022_022127Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211751,
    "items_db": 213573,
    "items_missing_in_db": 45,
    "codes_upstream": 87032,
    "codes_db": 258262,
    "codes_missing_in_db": 14,
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
  "csv_sha256": "d0a059390ed093a84603aadababaf4c9c9824b190c41adcb84ccc86c48f05077",
  "csv_size_bytes": 26894840,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261022_022127Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211751,
  "items_db": 213573,
  "items_missing_in_db": 45,
  "codes_upstream": 87032,
  "codes_db": 258262,
  "codes_missing_in_db": 14,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 45,
  "db_inserted_codes": 14
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258321,
  "distinct_bl_part_id": 178345,
  "null_boid": 180141,
  "null_weight": 102883,
  "null_bk_part_id": 59,
  "null_bk_part_key": 59,
  "null_api_item_type": 59,
  "null_brikick_name": 59,
  "null_part_name": 104600,
  "null_element_id": 175084,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180141`
- null_weight: `102883`
- corruption_pattern_count: `0`
