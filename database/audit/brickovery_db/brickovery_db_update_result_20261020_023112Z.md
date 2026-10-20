# Brikick DB Post-Update Report

- created_at_utc: `20261020_023112Z`
- db_path: `database/brickovery.db`
- db_sha256: `feb5dfc92e30c3c9dcb25890f71993f5f44928945a94a192891e24e9729d6bd4`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261020_023101Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261020_023101Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "8244d9827522fd68f7b7ad8b0b0e30a5812ed74f40c11286f4386dc33e98eea1",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261020_023101Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211687,
    "items_db": 213538,
    "items_missing_in_db": 16,
    "codes_upstream": 87015,
    "codes_db": 258220,
    "codes_missing_in_db": 4,
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
  "csv_sha256": "3e444954aa2cdfc910099ad571ce8187da830184ecaab939c76aea9670e939fd",
  "csv_size_bytes": 26892473,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261020_023101Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211687,
  "items_db": 213538,
  "items_missing_in_db": 16,
  "codes_upstream": 87015,
  "codes_db": 258220,
  "codes_missing_in_db": 4,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 16,
  "db_inserted_codes": 4
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258240,
  "distinct_bl_part_id": 178286,
  "null_boid": 180060,
  "null_weight": 102804,
  "null_bk_part_id": 20,
  "null_bk_part_key": 20,
  "null_api_item_type": 20,
  "null_brikick_name": 20,
  "null_part_name": 104519,
  "null_element_id": 175003,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180060`
- null_weight: `102804`
- corruption_pattern_count: `0`
