# Brikick DB Post-Update Report

- created_at_utc: `20260716_012950Z`
- db_path: `database/brickovery.db`
- db_sha256: `87b155fa8e557426ec4fc577261b2487231f1ee4f8986713629ec53b877f3bb3`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260716_012939Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260716_012939Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "9a603be2c15804e29f1b210ae3f93c2fbcf1afeee3da0ff11014b59539012f27",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260716_012939Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207865,
    "items_db": 208551,
    "items_missing_in_db": 6,
    "codes_upstream": 85366,
    "codes_db": 251151,
    "codes_missing_in_db": 2,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "75bd27df8f022b060f696697c68f6aa0a110dde2299b0df7729c93c55e71b1e9",
  "csv_size_bytes": 26487364,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260716_012939Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207865,
  "items_db": 208551,
  "items_missing_in_db": 6,
  "codes_upstream": 85366,
  "codes_db": 251151,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 6,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251159,
  "distinct_bl_part_id": 173777,
  "null_boid": 172983,
  "null_weight": 96330,
  "null_bk_part_id": 8,
  "null_bk_part_key": 8,
  "null_api_item_type": 8,
  "null_brikick_name": 8,
  "null_part_name": 97438,
  "null_element_id": 167922,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172983`
- null_weight: `96330`
- corruption_pattern_count: `0`
