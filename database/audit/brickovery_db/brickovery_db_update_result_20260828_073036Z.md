# Brikick DB Post-Update Report

- created_at_utc: `20260828_073036Z`
- db_path: `database/brickovery.db`
- db_sha256: `fb7de7c99b3638e23c0de4d97da56f739f7d7cf32efa4c3d1cc6aaf80ea6dbb5`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260828_073024Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260828_073024Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "2125515f8bd2edd29d697f5bf59758ed7140fcba4a4e7b792323901c33916ea1",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260828_073024Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209889,
    "items_db": 210691,
    "items_missing_in_db": 13,
    "codes_upstream": 86365,
    "codes_db": 254321,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "7c066c7436f4686358981321a0611c2e08b5a78031873aa71c1b3b8295e2c498",
  "csv_size_bytes": 26667698,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260828_073024Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209889,
  "items_db": 210691,
  "items_missing_in_db": 13,
  "codes_upstream": 86365,
  "codes_db": 254321,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 13,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254334,
  "distinct_bl_part_id": 175732,
  "null_boid": 176157,
  "null_weight": 99113,
  "null_bk_part_id": 13,
  "null_bk_part_key": 13,
  "null_api_item_type": 13,
  "null_brikick_name": 13,
  "null_part_name": 100613,
  "null_element_id": 171097,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176157`
- null_weight: `99113`
- corruption_pattern_count: `0`
