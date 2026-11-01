# Brikick DB Post-Update Report

- created_at_utc: `20261101_031131Z`
- db_path: `database/brickovery.db`
- db_sha256: `d40f22e6108f0c1e0fe24ca40cd8ab182bc1ecdb9157a09c9cd25ca042415202`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261101_031119Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261101_031119Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "9e58f4866f2f603e27665419851d60e0f75ac35fc76a868d38fff67d9e9ad02c",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261101_031119Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211996,
    "items_db": 213869,
    "items_missing_in_db": 5,
    "codes_upstream": 87127,
    "codes_db": 258662,
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
  "csv_sha256": "f9b10782e490d9498adb6c56ed7f6de21c4b7cb3a7efccb434660aa82605271d",
  "csv_size_bytes": 26917665,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261101_031119Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211996,
  "items_db": 213869,
  "items_missing_in_db": 5,
  "codes_upstream": 87127,
  "codes_db": 258662,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 5,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258669,
  "distinct_bl_part_id": 178589,
  "null_boid": 180489,
  "null_weight": 103223,
  "null_bk_part_id": 7,
  "null_bk_part_key": 7,
  "null_api_item_type": 7,
  "null_brikick_name": 7,
  "null_part_name": 104948,
  "null_element_id": 175432,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180489`
- null_weight: `103223`
- corruption_pattern_count: `0`
