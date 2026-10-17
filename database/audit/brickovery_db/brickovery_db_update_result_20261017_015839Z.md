# Brikick DB Post-Update Report

- created_at_utc: `20261017_015839Z`
- db_path: `database/brickovery.db`
- db_sha256: `b12448452e9e8257b1ea12087006b324847ad8f1d58ff91626f2b8504dd06f59`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261017_015831Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261017_015831Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "834baae6adac10b8f8f567c3725c8bdf58777599d59947e9a380e794c92dfd59",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261017_015831Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211637,
    "items_db": 213474,
    "items_missing_in_db": 19,
    "codes_upstream": 87003,
    "codes_db": 258142,
    "codes_missing_in_db": 7,
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
  "csv_sha256": "2ef66e1ba3462a071fdfa8a9f6dc134e4aaf1ab181f96a04aa0281b83324725f",
  "csv_size_bytes": 26887981,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261017_015831Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211637,
  "items_db": 213474,
  "items_missing_in_db": 19,
  "codes_upstream": 87003,
  "codes_db": 258142,
  "codes_missing_in_db": 7,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 19,
  "db_inserted_codes": 6
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258167,
  "distinct_bl_part_id": 178226,
  "null_boid": 179987,
  "null_weight": 102731,
  "null_bk_part_id": 25,
  "null_bk_part_key": 25,
  "null_api_item_type": 25,
  "null_brikick_name": 25,
  "null_part_name": 104446,
  "null_element_id": 174930,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179987`
- null_weight: `102731`
- corruption_pattern_count: `0`
