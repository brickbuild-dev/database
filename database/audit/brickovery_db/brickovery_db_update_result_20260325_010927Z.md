# Brikick DB Post-Update Report

- created_at_utc: `20260325_010927Z`
- db_path: `database/brickovery.db`
- db_sha256: `4564247c8a2b0c68a550462cc58efb0de5585fd02cd81a80561a6afef50ba3c8`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260325_010916Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260325_010916Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "a8af4799366192b2241d5c48d91dcc5e8dceb551727b05569c245de9f70104bf",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260325_010916Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203781,
    "items_db": 203871,
    "items_missing_in_db": 3,
    "codes_upstream": 84054,
    "codes_db": 244298,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "45722f5e5dce725457360dd37ddf1bb5553369ecd48e0fd8001c906f65981211",
  "csv_size_bytes": 26094790,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260325_010916Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203781,
  "items_db": 203871,
  "items_missing_in_db": 3,
  "codes_upstream": 84054,
  "codes_db": 244298,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 3,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 244302,
  "distinct_bl_part_id": 169576,
  "null_boid": 166134,
  "null_weight": 90463,
  "null_bk_part_id": 4,
  "null_bk_part_key": 4,
  "null_api_item_type": 4,
  "null_brikick_name": 4,
  "null_part_name": 90581,
  "null_element_id": 161065,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `166134`
- null_weight: `90463`
- corruption_pattern_count: `0`
