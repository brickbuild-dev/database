# Brikick DB Post-Update Report

- created_at_utc: `20261018_015825Z`
- db_path: `database/brickovery.db`
- db_sha256: `fbd187fb9616b666d23777967a236e16575754557ad4b8ec848bd353aea3e6f4`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261018_015815Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261018_015815Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "e27efdc2a683265c197e00e0a020b11810e1ca78a3f4984b73d4b730412d876a",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261018_015815Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211652,
    "items_db": 213493,
    "items_missing_in_db": 17,
    "codes_upstream": 87005,
    "codes_db": 258167,
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
  "csv_sha256": "c6e82cfe46526b97c7302af5ac6f4d9b28efa4019c946864a7d308612e496a1d",
  "csv_size_bytes": 26889440,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261018_015815Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211652,
  "items_db": 213493,
  "items_missing_in_db": 17,
  "codes_upstream": 87005,
  "codes_db": 258167,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 17,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258186,
  "distinct_bl_part_id": 178242,
  "null_boid": 180006,
  "null_weight": 102750,
  "null_bk_part_id": 19,
  "null_bk_part_key": 19,
  "null_api_item_type": 19,
  "null_brikick_name": 19,
  "null_part_name": 104465,
  "null_element_id": 174949,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180006`
- null_weight: `102750`
- corruption_pattern_count: `0`
