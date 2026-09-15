# Brikick DB Post-Update Report

- created_at_utc: `20260915_022108Z`
- db_path: `database/brickovery.db`
- db_sha256: `48cb97fd57315229480e3d0486b98e2249563cffc4c12b480a88f042a138635f`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260915_022059Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260915_022059Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "025535dec86c2d63bbc81af548b74e1d145c3e43970a9d21a812893c895ffbd5",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260915_022059Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210756,
    "items_db": 211553,
    "items_missing_in_db": 65,
    "codes_upstream": 86665,
    "codes_db": 255509,
    "codes_missing_in_db": 11,
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
  "csv_sha256": "4dc75152531ec4c9ad89e7be1d4c0bae651c5e17cfb26d1bc66dda8a6bdddb5f",
  "csv_size_bytes": 26736710,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260915_022059Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210756,
  "items_db": 211553,
  "items_missing_in_db": 65,
  "codes_upstream": 86665,
  "codes_db": 255509,
  "codes_missing_in_db": 11,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 65,
  "db_inserted_codes": 11
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255585,
  "distinct_bl_part_id": 176433,
  "null_boid": 177408,
  "null_weight": 100303,
  "null_bk_part_id": 76,
  "null_bk_part_key": 76,
  "null_api_item_type": 76,
  "null_brikick_name": 76,
  "null_part_name": 101864,
  "null_element_id": 172348,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177408`
- null_weight: `100303`
- corruption_pattern_count: `0`
