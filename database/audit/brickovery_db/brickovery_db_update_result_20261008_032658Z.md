# Brikick DB Post-Update Report

- created_at_utc: `20261008_032658Z`
- db_path: `database/brickovery.db`
- db_sha256: `d687b909d70962048e20d02a4c3bce7c2448e7335612107ea14de9ef96e84bcf`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261008_032647Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261008_032647Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "8280bd6fd44552d0b0c11313f9a5c066b1b600cd6df5af313c3a15ad470c2180",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261008_032647Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211530,
    "items_db": 213351,
    "items_missing_in_db": 21,
    "codes_upstream": 86906,
    "codes_db": 257903,
    "codes_missing_in_db": 21,
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
  "csv_sha256": "8355bf0ab71a04da6adc2a640939b46cff7902f873f7e1faaf7c9cfe89344f23",
  "csv_size_bytes": 26873968,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261008_032647Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211530,
  "items_db": 213351,
  "items_missing_in_db": 21,
  "codes_upstream": 86906,
  "codes_db": 257903,
  "codes_missing_in_db": 21,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 21,
  "db_inserted_codes": 21
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 257945,
  "distinct_bl_part_id": 178114,
  "null_boid": 179765,
  "null_weight": 102555,
  "null_bk_part_id": 42,
  "null_bk_part_key": 42,
  "null_api_item_type": 42,
  "null_brikick_name": 42,
  "null_part_name": 104224,
  "null_element_id": 174708,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179765`
- null_weight: `102555`
- corruption_pattern_count: `0`
