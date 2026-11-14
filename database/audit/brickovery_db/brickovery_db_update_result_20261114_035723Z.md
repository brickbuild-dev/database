# Brikick DB Post-Update Report

- created_at_utc: `20261114_035723Z`
- db_path: `database/brickovery.db`
- db_sha256: `c7bcbd436cd0810fef93db0e6868a5d160e3ce2e481db90969564605aaab68c8`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261114_035715Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261114_035715Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "4d1c01c12410291d76410348aa66a76659e3c358ffe684ad268f5c23feae9f2e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261114_035715Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212090,
    "items_db": 213969,
    "items_missing_in_db": 1,
    "codes_upstream": 87181,
    "codes_db": 258811,
    "codes_missing_in_db": 6,
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
  "csv_sha256": "c2644a8dd1b674f24c0bbb5ec85c0caf6ba9596cc96badc63d6dead89c67b347",
  "csv_size_bytes": 26926251,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261114_035715Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212090,
  "items_db": 213969,
  "items_missing_in_db": 1,
  "codes_upstream": 87181,
  "codes_db": 258811,
  "codes_missing_in_db": 6,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 1,
  "db_inserted_codes": 6
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258818,
  "distinct_bl_part_id": 178673,
  "null_boid": 180638,
  "null_weight": 103350,
  "null_bk_part_id": 7,
  "null_bk_part_key": 7,
  "null_api_item_type": 7,
  "null_brikick_name": 7,
  "null_part_name": 105097,
  "null_element_id": 175581,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180638`
- null_weight: `103350`
- corruption_pattern_count: `0`
