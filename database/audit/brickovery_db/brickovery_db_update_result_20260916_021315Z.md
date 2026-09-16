# Brikick DB Post-Update Report

- created_at_utc: `20260916_021315Z`
- db_path: `database/brickovery.db`
- db_sha256: `b5e6bee3d7b1cf4b5a542fd7d46f324a26b6c3adc7b040a9a84ea0454429b3e6`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260916_021306Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260916_021306Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "041677c6d88851607ed14158eff78014168dfa5010546542920b15a72708e3f6",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260916_021306Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210776,
    "items_db": 211618,
    "items_missing_in_db": 25,
    "codes_upstream": 86685,
    "codes_db": 255585,
    "codes_missing_in_db": 20,
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
  "csv_sha256": "eedb6dfa064455b303d9f8c4988b5c5c52a25d9f46f05479b98843e95bce7465",
  "csv_size_bytes": 26741171,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260916_021306Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210776,
  "items_db": 211618,
  "items_missing_in_db": 25,
  "codes_upstream": 86685,
  "codes_db": 255585,
  "codes_missing_in_db": 20,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 25,
  "db_inserted_codes": 20
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255630,
  "distinct_bl_part_id": 176456,
  "null_boid": 177453,
  "null_weight": 100340,
  "null_bk_part_id": 45,
  "null_bk_part_key": 45,
  "null_api_item_type": 45,
  "null_brikick_name": 45,
  "null_part_name": 101909,
  "null_element_id": 172393,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177453`
- null_weight: `100340`
- corruption_pattern_count: `0`
