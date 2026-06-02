# Brikick DB Post-Update Report

- created_at_utc: `20260602_023533Z`
- db_path: `database/brickovery.db`
- db_sha256: `25bbe95cde90f2223689a46a1623a0419334bb2b8c4cdd27f429ce831bd2690a`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260602_023521Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260602_023521Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "aaf8dbb381a2652d5ae91b0fae745ff0c68c31323e049392e03c0f00dfa91ccb",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260602_023521Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 206464,
    "items_db": 206682,
    "items_missing_in_db": 367,
    "codes_upstream": 84426,
    "codes_db": 248356,
    "codes_missing_in_db": 16,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "e9ca066dff1801bdb86ee37bab45f629097626a24e6fd3528b57509604f9c7df",
  "csv_size_bytes": 26325699,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260602_023521Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 206464,
  "items_db": 206682,
  "items_missing_in_db": 367,
  "codes_upstream": 84426,
  "codes_db": 248356,
  "codes_missing_in_db": 16,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 367,
  "db_inserted_codes": 16
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248739,
  "distinct_bl_part_id": 172318,
  "null_boid": 170564,
  "null_weight": 94176,
  "null_bk_part_id": 383,
  "null_bk_part_key": 383,
  "null_api_item_type": 383,
  "null_brikick_name": 383,
  "null_part_name": 95018,
  "null_element_id": 165502,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `170564`
- null_weight: `94176`
- corruption_pattern_count: `0`
