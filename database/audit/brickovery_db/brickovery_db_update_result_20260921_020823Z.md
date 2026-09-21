# Brikick DB Post-Update Report

- created_at_utc: `20260921_020823Z`
- db_path: `database/brickovery.db`
- db_sha256: `13abe0eb1857d1da5ead01460e82c1f4a38c2552c8e261d6686a39e4e1d7309e`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260921_020814Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260921_020814Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "b9f2636304a0db01c77383d28ef8905c4d342327ca263d83d4bfc98c9df764b6",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260921_020814Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211063,
    "items_db": 211698,
    "items_missing_in_db": 234,
    "codes_upstream": 86708,
    "codes_db": 255708,
    "codes_missing_in_db": 5,
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
  "csv_sha256": "61cfd81d8f171080205ca5670cd18007be7166cf143f2ba01045d1f526ca7cd3",
  "csv_size_bytes": 26748258,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260921_020814Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211063,
  "items_db": 211698,
  "items_missing_in_db": 234,
  "codes_upstream": 86708,
  "codes_db": 255708,
  "codes_missing_in_db": 5,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 234,
  "db_inserted_codes": 5
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255947,
  "distinct_bl_part_id": 176744,
  "null_boid": 177770,
  "null_weight": 100636,
  "null_bk_part_id": 239,
  "null_bk_part_key": 239,
  "null_api_item_type": 239,
  "null_brikick_name": 239,
  "null_part_name": 102226,
  "null_element_id": 172710,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177770`
- null_weight: `100636`
- corruption_pattern_count: `0`
