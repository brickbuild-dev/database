# Brikick DB Post-Update Report

- created_at_utc: `20261011_024020Z`
- db_path: `database/brickovery.db`
- db_sha256: `6772b31882102a291e0129cc08aba3ec4ac9e43cb07bac2e4ec13f2fd322d94a`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261011_024012Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261011_024012Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "9d1eb80c29831e7efbea2ee5521a37116d8e857679d33cd98c1e0da89ae03622",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261011_024012Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211578,
    "items_db": 213408,
    "items_missing_in_db": 17,
    "codes_upstream": 86955,
    "codes_db": 258031,
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
  "csv_sha256": "f427cd142168f213ec6c0e2fd11253ce3421ab2036b2d7d7e6b047028ac0e07d",
  "csv_size_bytes": 26881505,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261011_024012Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211578,
  "items_db": 213408,
  "items_missing_in_db": 17,
  "codes_upstream": 86955,
  "codes_db": 258031,
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
  "brickovery_db_rows": 258050,
  "distinct_bl_part_id": 178165,
  "null_boid": 179870,
  "null_weight": 102626,
  "null_bk_part_id": 19,
  "null_bk_part_key": 19,
  "null_api_item_type": 19,
  "null_brikick_name": 19,
  "null_part_name": 104329,
  "null_element_id": 174813,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179870`
- null_weight: `102626`
- corruption_pattern_count: `0`
