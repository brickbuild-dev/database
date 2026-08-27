# Brikick DB Post-Update Report

- created_at_utc: `20260827_053422Z`
- db_path: `database/brickovery.db`
- db_sha256: `58e3408a152411273789bed555d4f246565a7332a42ba165d43c16056f69edda`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260827_053410Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260827_053410Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "1c910388dc39c2543ce7fd7cf5fec88175adb42d8cab75ba4ddb0927250bc28f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260827_053410Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209876,
    "items_db": 210650,
    "items_missing_in_db": 41,
    "codes_upstream": 86364,
    "codes_db": 254253,
    "codes_missing_in_db": 27,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "a167fbd3d36b8bf25d23a347094940067adf7944e4e6aa98fb5a4a4dd3c99295",
  "csv_size_bytes": 26663617,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260827_053410Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209876,
  "items_db": 210650,
  "items_missing_in_db": 41,
  "codes_upstream": 86364,
  "codes_db": 254253,
  "codes_missing_in_db": 27,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 41,
  "db_inserted_codes": 27
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254321,
  "distinct_bl_part_id": 175727,
  "null_boid": 176144,
  "null_weight": 99100,
  "null_bk_part_id": 68,
  "null_bk_part_key": 68,
  "null_api_item_type": 68,
  "null_brikick_name": 68,
  "null_part_name": 100600,
  "null_element_id": 171084,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176144`
- null_weight: `99100`
- corruption_pattern_count: `0`
