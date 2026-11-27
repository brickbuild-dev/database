# Brikick DB Post-Update Report

- created_at_utc: `20261127_080143Z`
- db_path: `database/brickovery.db`
- db_sha256: `fbbc2482656fdd010994fb6823e008fdcbdcc1458000cf6ef3e473da9e263ed6`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261127_080135Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261127_080135Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "6024b3a6f261ff8a8706eb413737e8ce73ff40a1defa76e5c837bc69aaf5a5ef",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261127_080135Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212217,
    "items_db": 214094,
    "items_missing_in_db": 9,
    "codes_upstream": 87201,
    "codes_db": 258961,
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
  "csv_sha256": "0ac9ba75783757e7cde05ada2723c71ca74c66384adc4f92e9d5e245731920b7",
  "csv_size_bytes": 26934995,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261127_080135Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212217,
  "items_db": 214094,
  "items_missing_in_db": 9,
  "codes_upstream": 87201,
  "codes_db": 258961,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 9,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258970,
  "distinct_bl_part_id": 178786,
  "null_boid": 180790,
  "null_weight": 103496,
  "null_bk_part_id": 9,
  "null_bk_part_key": 9,
  "null_api_item_type": 9,
  "null_brikick_name": 9,
  "null_part_name": 105249,
  "null_element_id": 175733,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180790`
- null_weight: `103496`
- corruption_pattern_count: `0`
