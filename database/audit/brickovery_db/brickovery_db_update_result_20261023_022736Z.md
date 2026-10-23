# Brikick DB Post-Update Report

- created_at_utc: `20261023_022736Z`
- db_path: `database/brickovery.db`
- db_sha256: `54517a6feda3c5ac64337cbeec6cdb0b9ca4e0e165f17deaab847f78943b33e6`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261023_022725Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261023_022725Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "2d039648e6317802e962dd4488cac59c550848991aa5130bcba20f46fb6dc0fc",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261023_022725Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211762,
    "items_db": 213618,
    "items_missing_in_db": 11,
    "codes_upstream": 87032,
    "codes_db": 258321,
    "codes_missing_in_db": 0,
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
  "csv_sha256": "342ffc14e5b182a42cd45172b5b37e1af494b936d21f20aed374bb33663ddd9e",
  "csv_size_bytes": 26898203,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261023_022725Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211762,
  "items_db": 213618,
  "items_missing_in_db": 11,
  "codes_upstream": 87032,
  "codes_db": 258321,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 11,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258332,
  "distinct_bl_part_id": 178356,
  "null_boid": 180152,
  "null_weight": 102893,
  "null_bk_part_id": 11,
  "null_bk_part_key": 11,
  "null_api_item_type": 11,
  "null_brikick_name": 11,
  "null_part_name": 104611,
  "null_element_id": 175095,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180152`
- null_weight: `102893`
- corruption_pattern_count: `0`
