# Brikick DB Post-Update Report

- created_at_utc: `20261120_044909Z`
- db_path: `database/brickovery.db`
- db_sha256: `b376b6f243732fc6576d1aee4341e41ab30a533cfa093ccf0b7b3ce36a9ddf71`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261120_044857Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261120_044857Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "f688f788cb1fb49e45b441f4f41456d18bbd9c105667237675016aa50b1b8bad",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261120_044857Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212168,
    "items_db": 214050,
    "items_missing_in_db": 3,
    "codes_upstream": 87191,
    "codes_db": 258908,
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
  "csv_sha256": "611a25a02fd5a36be0c43b85b626e6a40a0cc8e8fcbb36bafd13acaec80e1c29",
  "csv_size_bytes": 26931916,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261120_044857Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212168,
  "items_db": 214050,
  "items_missing_in_db": 3,
  "codes_upstream": 87191,
  "codes_db": 258908,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 3,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258911,
  "distinct_bl_part_id": 178752,
  "null_boid": 180731,
  "null_weight": 103437,
  "null_bk_part_id": 3,
  "null_bk_part_key": 3,
  "null_api_item_type": 3,
  "null_brikick_name": 3,
  "null_part_name": 105190,
  "null_element_id": 175674,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180731`
- null_weight: `103437`
- corruption_pattern_count: `0`
