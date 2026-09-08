# Brikick DB Post-Update Report

- created_at_utc: `20260908_020527Z`
- db_path: `database/brickovery.db`
- db_sha256: `65211cff91d9874af887657d901d0283517212640d5fbd65588944d9ccec8b13`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260908_020516Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260908_020516Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "0bc1fb3e712a0deb65e6b8d0a0773e40b135be6a236803c2c28093fb3bd11e2b",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260908_020516Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210458,
    "items_db": 211288,
    "items_missing_in_db": 10,
    "codes_upstream": 86528,
    "codes_db": 255096,
    "codes_missing_in_db": 9,
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
  "csv_sha256": "814868f63ebd8adbd2cf9cf465ae2841582b44a780eac5a7b55fce3e6f0197f1",
  "csv_size_bytes": 26713108,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260908_020516Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210458,
  "items_db": 211288,
  "items_missing_in_db": 10,
  "codes_upstream": 86528,
  "codes_db": 255096,
  "codes_missing_in_db": 9,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 10,
  "db_inserted_codes": 9
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255115,
  "distinct_bl_part_id": 176148,
  "null_boid": 176938,
  "null_weight": 99847,
  "null_bk_part_id": 19,
  "null_bk_part_key": 19,
  "null_api_item_type": 19,
  "null_brikick_name": 19,
  "null_part_name": 101394,
  "null_element_id": 171878,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176938`
- null_weight: `99847`
- corruption_pattern_count: `0`
