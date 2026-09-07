# Brikick DB Post-Update Report

- created_at_utc: `20260907_014341Z`
- db_path: `database/brickovery.db`
- db_sha256: `0121b61fee4c455bcc264595bd9740ef8095404f3375bd5b39733701b26ee6f0`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260907_014330Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260907_014330Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "852fc6e4d397659734e65961102fb282d328208652961ebf09b3091493ab8d9f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260907_014330Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210347,
    "items_db": 211147,
    "items_missing_in_db": 37,
    "codes_upstream": 86458,
    "codes_db": 254868,
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
  "csv_sha256": "7645e3968c18faacdecb0728724bae4531ba9f99b991a0eab907b48f86db738e",
  "csv_size_bytes": 26699888,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260907_014330Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210347,
  "items_db": 211147,
  "items_missing_in_db": 37,
  "codes_upstream": 86458,
  "codes_db": 254868,
  "codes_missing_in_db": 26,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 37,
  "db_inserted_codes": 26
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254931,
  "distinct_bl_part_id": 176058,
  "null_boid": 176754,
  "null_weight": 99693,
  "null_bk_part_id": 63,
  "null_bk_part_key": 63,
  "null_api_item_type": 63,
  "null_brikick_name": 63,
  "null_part_name": 101210,
  "null_element_id": 171694,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176754`
- null_weight: `99693`
- corruption_pattern_count: `0`
