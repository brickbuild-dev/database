# Brikick DB Post-Update Report

- created_at_utc: `20260819_003938Z`
- db_path: `database/brickovery.db`
- db_sha256: `dc44a797e9b972dc2da4fbaa12034e7bbf6f90f5514d88fa6a4664ba71130358`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260819_003927Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260819_003927Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "b17cfeec20a5dad359cc21dd71cdc52f518e3398dac3a8b1e539b68815489f15",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260819_003927Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209672,
    "items_db": 210457,
    "items_missing_in_db": 5,
    "codes_upstream": 86234,
    "codes_db": 253939,
    "codes_missing_in_db": 3,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "412fb4cb8f972eaa213471afc63cb7722126fcccdd23076cadeeb20e56164c21",
  "csv_size_bytes": 26645316,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260819_003927Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209672,
  "items_db": 210457,
  "items_missing_in_db": 5,
  "codes_upstream": 86234,
  "codes_db": 253939,
  "codes_missing_in_db": 3,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 5,
  "db_inserted_codes": 3
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253947,
  "distinct_bl_part_id": 175507,
  "null_boid": 175770,
  "null_weight": 98751,
  "null_bk_part_id": 8,
  "null_bk_part_key": 8,
  "null_api_item_type": 8,
  "null_brikick_name": 8,
  "null_part_name": 100226,
  "null_element_id": 170710,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175770`
- null_weight: `98751`
- corruption_pattern_count: `0`
