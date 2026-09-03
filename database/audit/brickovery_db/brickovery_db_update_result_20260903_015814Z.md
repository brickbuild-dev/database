# Brikick DB Post-Update Report

- created_at_utc: `20260903_015814Z`
- db_path: `database/brickovery.db`
- db_sha256: `5423e0b2f16f2b599339c45b7528dea3e1bd9a5af1a0049a3e94106cd2fa11ed`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260903_015803Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260903_015803Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "b5da06d4dd6e0c3f7762ff3bd0cf9cef0d46382604bde1311f97b9a67716e219",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260903_015803Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210202,
    "items_db": 210950,
    "items_missing_in_db": 73,
    "codes_upstream": 86392,
    "codes_db": 254610,
    "codes_missing_in_db": 26,
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
  "csv_sha256": "7b9a0c4172b46518092fc4711bc173d141c912c1021f961e5366738da615b7c4",
  "csv_size_bytes": 26684760,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260903_015803Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210202,
  "items_db": 210950,
  "items_missing_in_db": 73,
  "codes_upstream": 86392,
  "codes_db": 254610,
  "codes_missing_in_db": 26,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 73,
  "db_inserted_codes": 25
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254708,
  "distinct_bl_part_id": 175913,
  "null_boid": 176531,
  "null_weight": 99483,
  "null_bk_part_id": 98,
  "null_bk_part_key": 98,
  "null_api_item_type": 98,
  "null_brikick_name": 98,
  "null_part_name": 100987,
  "null_element_id": 171471,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176531`
- null_weight: `99483`
- corruption_pattern_count: `0`
