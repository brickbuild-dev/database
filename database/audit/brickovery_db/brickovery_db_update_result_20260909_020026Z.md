# Brikick DB Post-Update Report

- created_at_utc: `20260909_020026Z`
- db_path: `database/brickovery.db`
- db_sha256: `ad083b79582fb9e64b16db1eb5d9d008c7015891e86a22edca530dee55a70b17`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260909_020014Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260909_020014Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "e9ba698a5570f329b5b678fb7f437c88a517bd8c3fed2be2151c2c893402265a",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260909_020014Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210521,
    "items_db": 211298,
    "items_missing_in_db": 63,
    "codes_upstream": 86572,
    "codes_db": 255115,
    "codes_missing_in_db": 44,
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
  "csv_sha256": "3a8955f386c27d3890eb5b172e0f0316aac665b439268bf9bffd19800d945ada",
  "csv_size_bytes": 26714235,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260909_020014Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210521,
  "items_db": 211298,
  "items_missing_in_db": 63,
  "codes_upstream": 86572,
  "codes_db": 255115,
  "codes_missing_in_db": 44,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 63,
  "db_inserted_codes": 43
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255221,
  "distinct_bl_part_id": 176210,
  "null_boid": 177044,
  "null_weight": 99952,
  "null_bk_part_id": 106,
  "null_bk_part_key": 106,
  "null_api_item_type": 106,
  "null_brikick_name": 106,
  "null_part_name": 101500,
  "null_element_id": 171984,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177044`
- null_weight: `99952`
- corruption_pattern_count: `0`
