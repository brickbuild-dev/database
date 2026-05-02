# Brikick DB Post-Update Report

- created_at_utc: `20260502_013407Z`
- db_path: `database/brickovery.db`
- db_sha256: `d8c24ac7174e750fd2bffbd1dde609fe38cf516aef57e9eeded0029fdddd87e2`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260502_013356Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260502_013356Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "88200d815a3e57bda8621185510399644cdd57ffd2e130252775074bc566dda3",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260502_013356Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205532,
    "items_db": 205767,
    "items_missing_in_db": 139,
    "codes_upstream": 84517,
    "codes_db": 246602,
    "codes_missing_in_db": 54,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "b300e6e8a2438f49b305cb6c80d8b82988d4c29166c854ddc9fdc09fb913d641",
  "csv_size_bytes": 26224778,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260502_013356Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205532,
  "items_db": 205767,
  "items_missing_in_db": 139,
  "codes_upstream": 84517,
  "codes_db": 246602,
  "codes_missing_in_db": 54,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 139,
  "db_inserted_codes": 54
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246795,
  "distinct_bl_part_id": 171454,
  "null_boid": 168621,
  "null_weight": 92682,
  "null_bk_part_id": 193,
  "null_bk_part_key": 193,
  "null_api_item_type": 193,
  "null_brikick_name": 193,
  "null_part_name": 93074,
  "null_element_id": 163558,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168621`
- null_weight: `92682`
- corruption_pattern_count: `0`
