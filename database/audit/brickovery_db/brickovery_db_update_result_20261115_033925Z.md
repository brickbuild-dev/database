# Brikick DB Post-Update Report

- created_at_utc: `20261115_033925Z`
- db_path: `database/brickovery.db`
- db_sha256: `fec203287d6149566c19ccfbf619b8ecab6739f1c254df57d5878d029ef2b827`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261115_033915Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261115_033915Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "81a293cdd6766b75049f37704ef5e2f8cfd1be59c9c0824cdaa9c617411933a7",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261115_033915Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212113,
    "items_db": 213970,
    "items_missing_in_db": 24,
    "codes_upstream": 87181,
    "codes_db": 258818,
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
  "csv_sha256": "bc3549a69ae8b8518f16e0cc73ea75573842622168370c5125ef2c685f7f7e63",
  "csv_size_bytes": 26926657,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261115_033915Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212113,
  "items_db": 213970,
  "items_missing_in_db": 24,
  "codes_upstream": 87181,
  "codes_db": 258818,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 24,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258843,
  "distinct_bl_part_id": 178695,
  "null_boid": 180663,
  "null_weight": 103369,
  "null_bk_part_id": 25,
  "null_bk_part_key": 25,
  "null_api_item_type": 25,
  "null_brikick_name": 25,
  "null_part_name": 105122,
  "null_element_id": 175606,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180663`
- null_weight: `103369`
- corruption_pattern_count: `0`
