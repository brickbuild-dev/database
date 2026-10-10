# Brikick DB Post-Update Report

- created_at_utc: `20261010_031111Z`
- db_path: `database/brickovery.db`
- db_sha256: `cdf55a4bce343611bda8e99a0f4f42542d21566d3fce3bf78e2d5385af008a3d`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261010_031100Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261010_031100Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "278e5e9ec424d358b3644641db4fa6967e0c35265f0672103f6fd75efa2f7548",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261010_031100Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211561,
    "items_db": 213398,
    "items_missing_in_db": 10,
    "codes_upstream": 86953,
    "codes_db": 258008,
    "codes_missing_in_db": 13,
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
  "csv_sha256": "e0af80f3b2ed63222295d32adb6e49396d8b77c936c4d6e55c4f4ba494e3e02f",
  "csv_size_bytes": 26880149,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261010_031100Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211561,
  "items_db": 213398,
  "items_missing_in_db": 10,
  "codes_upstream": 86953,
  "codes_db": 258008,
  "codes_missing_in_db": 13,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 10,
  "db_inserted_codes": 13
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258031,
  "distinct_bl_part_id": 178148,
  "null_boid": 179851,
  "null_weight": 102615,
  "null_bk_part_id": 23,
  "null_bk_part_key": 23,
  "null_api_item_type": 23,
  "null_brikick_name": 23,
  "null_part_name": 104310,
  "null_element_id": 174794,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179851`
- null_weight: `102615`
- corruption_pattern_count: `0`
