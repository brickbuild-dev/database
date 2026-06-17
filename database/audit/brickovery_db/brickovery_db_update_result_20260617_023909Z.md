# Brikick DB Post-Update Report

- created_at_utc: `20260617_023909Z`
- db_path: `database/brickovery.db`
- db_sha256: `c20363ea0f9a6b2804375dbaf43e979aa01e16ee64e082a651459e43a82e3c85`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260617_023858Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260617_023858Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "208db5089f9832e8f8e1be10f6d6fce4d91540a2ad1977f49587cfc7c8f80b2d",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260617_023858Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207248,
    "items_db": 207822,
    "items_missing_in_db": 44,
    "codes_upstream": 84874,
    "codes_db": 249898,
    "codes_missing_in_db": 21,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "d03aad625daabe1bf0c29bd04d9c325ec8ad7582729898638b55ef70fa0c8113",
  "csv_size_bytes": 26414560,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260617_023858Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207248,
  "items_db": 207822,
  "items_missing_in_db": 44,
  "codes_upstream": 84874,
  "codes_db": 249898,
  "codes_missing_in_db": 21,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 44,
  "db_inserted_codes": 19
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 249961,
  "distinct_bl_part_id": 173125,
  "null_boid": 171785,
  "null_weight": 95301,
  "null_bk_part_id": 63,
  "null_bk_part_key": 63,
  "null_api_item_type": 63,
  "null_brikick_name": 63,
  "null_part_name": 96240,
  "null_element_id": 166724,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171785`
- null_weight: `95301`
- corruption_pattern_count: `0`
