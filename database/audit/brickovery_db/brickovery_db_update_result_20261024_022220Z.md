# Brikick DB Post-Update Report

- created_at_utc: `20261024_022220Z`
- db_path: `database/brickovery.db`
- db_sha256: `ef2488906d65a127178297bf808faac1c34fb718f38497b67b0dff8b899f0ded`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261024_022210Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261024_022210Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "436e81630a59832f6cda3676665b732257ab344a7ca64884d5389d2adc70f3f8",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261024_022210Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211767,
    "items_db": 213629,
    "items_missing_in_db": 5,
    "codes_upstream": 87032,
    "codes_db": 258332,
    "codes_missing_in_db": 0,
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
  "csv_sha256": "22fdb44d3cf350e886af6d6f47e695bde1e11b805df3e8a9a4e6d8ee01487812",
  "csv_size_bytes": 26898814,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261024_022210Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211767,
  "items_db": 213629,
  "items_missing_in_db": 5,
  "codes_upstream": 87032,
  "codes_db": 258332,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 5,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258337,
  "distinct_bl_part_id": 178361,
  "null_boid": 180157,
  "null_weight": 102898,
  "null_bk_part_id": 5,
  "null_bk_part_key": 5,
  "null_api_item_type": 5,
  "null_brikick_name": 5,
  "null_part_name": 104616,
  "null_element_id": 175100,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180157`
- null_weight: `102898`
- corruption_pattern_count: `0`
