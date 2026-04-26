# Brikick DB Post-Update Report

- created_at_utc: `20260426_013132Z`
- db_path: `database/brickovery.db`
- db_sha256: `39b152b19650428bed0066cbc63c76a551366eebe308f900c3406a7fa047b9c7`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260426_013121Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260426_013121Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "e550aa92c3a0f80b88dca99299b7301425987ad6259fd4f0abbbd2c2e68edea2",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260426_013121Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205290,
    "items_db": 205654,
    "items_missing_in_db": 8,
    "codes_upstream": 84259,
    "codes_db": 246288,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "205a1bf23f2dfe752cdd10a626900a1f0cd9a642aeff22e945f278e5fd366375",
  "csv_size_bytes": 26206622,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260426_013121Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205290,
  "items_db": 205654,
  "items_missing_in_db": 8,
  "codes_upstream": 84259,
  "codes_db": 246288,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 8,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246297,
  "distinct_bl_part_id": 171295,
  "null_boid": 168123,
  "null_weight": 92342,
  "null_bk_part_id": 9,
  "null_bk_part_key": 9,
  "null_api_item_type": 9,
  "null_brikick_name": 9,
  "null_part_name": 92576,
  "null_element_id": 163060,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168123`
- null_weight: `92342`
- corruption_pattern_count: `0`
