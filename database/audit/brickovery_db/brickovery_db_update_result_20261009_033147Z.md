# Brikick DB Post-Update Report

- created_at_utc: `20261009_033147Z`
- db_path: `database/brickovery.db`
- db_sha256: `9b4336da542cb7db0bdcc2c095d5596063dc7e86bbfbbb383490c1adf4917390`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261009_033137Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261009_033137Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "66651b7a88608b51ccc47e7aecff3ebbab0aeb1946ee39cf2003411cfad10bd4",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261009_033137Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211551,
    "items_db": 213372,
    "items_missing_in_db": 26,
    "codes_upstream": 86940,
    "codes_db": 257945,
    "codes_missing_in_db": 37,
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
  "csv_sha256": "42ee7a86361463898bfe412d982bfff06dec0b9942a2d582f3354545f9fe2918",
  "csv_size_bytes": 26876459,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261009_033137Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211551,
  "items_db": 213372,
  "items_missing_in_db": 26,
  "codes_upstream": 86940,
  "codes_db": 257945,
  "codes_missing_in_db": 37,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 26,
  "db_inserted_codes": 37
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258008,
  "distinct_bl_part_id": 178138,
  "null_boid": 179828,
  "null_weight": 102614,
  "null_bk_part_id": 63,
  "null_bk_part_key": 63,
  "null_api_item_type": 63,
  "null_brikick_name": 63,
  "null_part_name": 104287,
  "null_element_id": 174771,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179828`
- null_weight: `102614`
- corruption_pattern_count: `0`
