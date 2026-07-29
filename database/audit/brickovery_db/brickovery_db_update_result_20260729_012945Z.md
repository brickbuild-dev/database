# Brikick DB Post-Update Report

- created_at_utc: `20260729_012945Z`
- db_path: `database/brickovery.db`
- db_sha256: `2563a4c67590b4e162efa9a41ed5fa3c9bec233ffa51d8710e8b06070f55d9a6`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260729_012933Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260729_012933Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "eb5e31d5f12e03d5c08140755d81732f1bf5377be0d950631c930fa9313a921a",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260729_012933Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 208134,
    "items_db": 208847,
    "items_missing_in_db": 14,
    "codes_upstream": 85417,
    "codes_db": 251495,
    "codes_missing_in_db": 2,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "85bebd62936a17eb07c0221c1af3e5f08edf1fb544694dcae481cfb245924e76",
  "csv_size_bytes": 26506436,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260729_012933Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 208134,
  "items_db": 208847,
  "items_missing_in_db": 14,
  "codes_upstream": 85417,
  "codes_db": 251495,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 14,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251511,
  "distinct_bl_part_id": 174077,
  "null_boid": 173335,
  "null_weight": 96674,
  "null_bk_part_id": 16,
  "null_bk_part_key": 16,
  "null_api_item_type": 16,
  "null_brikick_name": 16,
  "null_part_name": 97790,
  "null_element_id": 168274,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `173335`
- null_weight: `96674`
- corruption_pattern_count: `0`
