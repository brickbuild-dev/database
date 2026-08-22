# Brikick DB Post-Update Report

- created_at_utc: `20260822_003721Z`
- db_path: `database/brickovery.db`
- db_sha256: `749904f981e53e0757ab71955f21f86977413619f17dad9d61637066bc903432`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260822_003711Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260822_003711Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "58a2ea8781bb2895a963cfc9b1ce7ef368a2d947b8624c5af82c4f6f8d546fe5",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260822_003711Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209778,
    "items_db": 210563,
    "items_missing_in_db": 13,
    "codes_upstream": 86299,
    "codes_db": 254084,
    "codes_missing_in_db": 34,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "1eb551fcdc89c17994d9ce3e7be43944a86c8b8c069984bc288691f837d25fe1",
  "csv_size_bytes": 26653699,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260822_003711Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209778,
  "items_db": 210563,
  "items_missing_in_db": 13,
  "codes_upstream": 86299,
  "codes_db": 254084,
  "codes_missing_in_db": 34,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 13,
  "db_inserted_codes": 33
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254130,
  "distinct_bl_part_id": 175620,
  "null_boid": 175953,
  "null_weight": 98932,
  "null_bk_part_id": 46,
  "null_bk_part_key": 46,
  "null_api_item_type": 46,
  "null_brikick_name": 46,
  "null_part_name": 100409,
  "null_element_id": 170893,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175953`
- null_weight: `98932`
- corruption_pattern_count: `0`
