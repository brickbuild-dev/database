# Brikick DB Post-Update Report

- created_at_utc: `20260901_022844Z`
- db_path: `database/brickovery.db`
- db_sha256: `d1a28be5a2d2fb5029cf449efde322e0fccc9213550671970a4e443e4467f4b1`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260901_022833Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260901_022833Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "494e89941b81f41add5124f93f78748c6ebe2fe7fbf389c6c3ef541760a89269",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260901_022833Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209925,
    "items_db": 210739,
    "items_missing_in_db": 6,
    "codes_upstream": 86354,
    "codes_db": 254392,
    "codes_missing_in_db": 2,
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
  "csv_sha256": "4e191093845f14b3b09ff461383e7e62d5e743ccf0dcc10d3622117d67aa9c30",
  "csv_size_bytes": 26671868,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260901_022833Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209925,
  "items_db": 210739,
  "items_missing_in_db": 6,
  "codes_upstream": 86354,
  "codes_db": 254392,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 6,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254400,
  "distinct_bl_part_id": 175765,
  "null_boid": 176223,
  "null_weight": 99178,
  "null_bk_part_id": 8,
  "null_bk_part_key": 8,
  "null_api_item_type": 8,
  "null_brikick_name": 8,
  "null_part_name": 100679,
  "null_element_id": 171163,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176223`
- null_weight: `99178`
- corruption_pattern_count: `0`
