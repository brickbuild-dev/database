# Brikick DB Post-Update Report

- created_at_utc: `20260418_035519Z`
- db_path: `database/brickovery.db`
- db_sha256: `277bb012026600dfad8fb10d6621f7bc0d0d9eb5f54db76d089b098b486c8b55`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260418_035507Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260418_035507Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "812ed90dd8db129072643cd90b7bba776949a92d49ad15579c29865a21dbd5c1",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260418_035507Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205223,
    "items_db": 205577,
    "items_missing_in_db": 1,
    "codes_upstream": 84162,
    "codes_db": 246102,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "19fc94f24f562fbd7ad7e5455e313e99a60a04dbf2e150ad4c619622c54b6997",
  "csv_size_bytes": 26196012,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260418_035507Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205223,
  "items_db": 205577,
  "items_missing_in_db": 1,
  "codes_upstream": 84162,
  "codes_db": 246102,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 1,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246103,
  "distinct_bl_part_id": 171218,
  "null_boid": 167933,
  "null_weight": 92234,
  "null_bk_part_id": 1,
  "null_bk_part_key": 1,
  "null_api_item_type": 1,
  "null_brikick_name": 1,
  "null_part_name": 92382,
  "null_element_id": 162866,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167933`
- null_weight: `92234`
- corruption_pattern_count: `0`
