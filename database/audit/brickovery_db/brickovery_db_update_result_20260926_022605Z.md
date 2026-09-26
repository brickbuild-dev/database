# Brikick DB Post-Update Report

- created_at_utc: `20260926_022605Z`
- db_path: `database/brickovery.db`
- db_sha256: `edf091c8bb2b5d4df638537e01e8a4ab0950a40fb694b00b03ddffe0e6b66bf4`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260926_022554Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260926_022554Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "35ef405bd68b275e05d475cc89f05de1cdb60e7bc589b7eb6c35cdf9f6211d67",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260926_022554Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211154,
    "items_db": 212056,
    "items_missing_in_db": 14,
    "codes_upstream": 86708,
    "codes_db": 256073,
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
  "csv_sha256": "833e1cae6877a0fca9f88662e93725e0303e290822541cdda4694c7487ce564d",
  "csv_size_bytes": 26767461,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260926_022554Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211154,
  "items_db": 212056,
  "items_missing_in_db": 14,
  "codes_upstream": 86708,
  "codes_db": 256073,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 14,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 256087,
  "distinct_bl_part_id": 176867,
  "null_boid": 177908,
  "null_weight": 100776,
  "null_bk_part_id": 14,
  "null_bk_part_key": 14,
  "null_api_item_type": 14,
  "null_brikick_name": 14,
  "null_part_name": 102366,
  "null_element_id": 172850,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177908`
- null_weight: `100776`
- corruption_pattern_count: `0`
