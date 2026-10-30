# Brikick DB Post-Update Report

- created_at_utc: `20261030_032450Z`
- db_path: `database/brickovery.db`
- db_sha256: `df1ad8d51f7804280c7f324fe827810783631aa2be4dca24f9eda9b3716b5368`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261030_032439Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261030_032439Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "cdbc9e60b6428f5751735be62697958dc7f0c0daddeb90f2f80d00fe0830437c",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261030_032439Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211990,
    "items_db": 213805,
    "items_missing_in_db": 62,
    "codes_upstream": 87125,
    "codes_db": 258567,
    "codes_missing_in_db": 32,
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
  "csv_sha256": "e82640d8ecca55bc48e8851d117b1a6bedf96efac1abb5049f3cc33f9f97c97e",
  "csv_size_bytes": 26912197,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261030_032439Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211990,
  "items_db": 213805,
  "items_missing_in_db": 62,
  "codes_upstream": 87125,
  "codes_db": 258567,
  "codes_missing_in_db": 32,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 62,
  "db_inserted_codes": 31
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258660,
  "distinct_bl_part_id": 178583,
  "null_boid": 180480,
  "null_weight": 103215,
  "null_bk_part_id": 93,
  "null_bk_part_key": 93,
  "null_api_item_type": 93,
  "null_brikick_name": 93,
  "null_part_name": 104939,
  "null_element_id": 175423,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180480`
- null_weight: `103215`
- corruption_pattern_count: `0`
