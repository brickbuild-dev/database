# Brikick DB Post-Update Report

- created_at_utc: `20260831_020708Z`
- db_path: `database/brickovery.db`
- db_sha256: `9950ae359e250149315993dbf89eec989a57b113bb1d996590afe97efa410fa6`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260831_020656Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260831_020656Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "f6b9b7fba9af523babf346934dc8ae80b27d496ddc78d8c411b720f827706286",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260831_020656Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209919,
    "items_db": 210729,
    "items_missing_in_db": 10,
    "codes_upstream": 86352,
    "codes_db": 254381,
    "codes_missing_in_db": 1,
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
  "csv_sha256": "433bed4ac042cbe727b78d55e271ea62d1eb5d7487387dffcb27badab95359b8",
  "csv_size_bytes": 26671254,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260831_020656Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209919,
  "items_db": 210729,
  "items_missing_in_db": 10,
  "codes_upstream": 86352,
  "codes_db": 254381,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 10,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254392,
  "distinct_bl_part_id": 175759,
  "null_boid": 176215,
  "null_weight": 99170,
  "null_bk_part_id": 11,
  "null_bk_part_key": 11,
  "null_api_item_type": 11,
  "null_brikick_name": 11,
  "null_part_name": 100671,
  "null_element_id": 171155,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176215`
- null_weight: `99170`
- corruption_pattern_count: `0`
