# Brikick DB Post-Update Report

- created_at_utc: `20260910_015535Z`
- db_path: `database/brickovery.db`
- db_sha256: `99a587d03e23c8f7f4e68b8b5e2597f2e5d7306254bd019396daa67f8d495c22`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260910_015526Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260910_015526Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "fe3c428fb0c7157e69c01fccba75da4139b69b847563d6cc72b1f202e4265d4f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260910_015526Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210623,
    "items_db": 211361,
    "items_missing_in_db": 114,
    "codes_upstream": 86606,
    "codes_db": 255227,
    "codes_missing_in_db": 41,
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
  "csv_sha256": "c010ea77b3eaea90b87616ac20b5cac1947dacd4f5c683b934e96dd9df62b55f",
  "csv_size_bytes": 26720693,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260910_015526Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210623,
  "items_db": 211361,
  "items_missing_in_db": 114,
  "codes_upstream": 86606,
  "codes_db": 255227,
  "codes_missing_in_db": 41,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 114,
  "db_inserted_codes": 41
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255382,
  "distinct_bl_part_id": 176315,
  "null_boid": 177205,
  "null_weight": 100110,
  "null_bk_part_id": 155,
  "null_bk_part_key": 155,
  "null_api_item_type": 155,
  "null_brikick_name": 155,
  "null_part_name": 101661,
  "null_element_id": 172145,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177205`
- null_weight: `100110`
- corruption_pattern_count: `0`
