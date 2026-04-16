# Brikick DB Post-Update Report

- created_at_utc: `20260416_012827Z`
- db_path: `database/brickovery.db`
- db_sha256: `7b33d49d7e227f0a85ca7cd9833e5c2c7f632f8099afc3c0b414162294988fc1`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260416_012816Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260416_012816Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "bce854a0e84f90f2be57cccf58663ec7349cd71502bcef5b3aca3a85b1d4279a",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260416_012816Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205205,
    "items_db": 205549,
    "items_missing_in_db": 4,
    "codes_upstream": 84160,
    "codes_db": 246068,
    "codes_missing_in_db": 4,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "e3faf5464602fa473761739d480b0861835762c32dfd673530903aa9b86411f5",
  "csv_size_bytes": 26194056,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260416_012816Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205205,
  "items_db": 205549,
  "items_missing_in_db": 4,
  "codes_upstream": 84160,
  "codes_db": 246068,
  "codes_missing_in_db": 4,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 4,
  "db_inserted_codes": 4
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246076,
  "distinct_bl_part_id": 171197,
  "null_boid": 167906,
  "null_weight": 92213,
  "null_bk_part_id": 8,
  "null_bk_part_key": 8,
  "null_api_item_type": 8,
  "null_brikick_name": 8,
  "null_part_name": 92355,
  "null_element_id": 162839,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167906`
- null_weight: `92213`
- corruption_pattern_count: `0`
