# Brikick DB Post-Update Report

- created_at_utc: `20260311_010236Z`
- db_path: `database/brickovery.db`
- db_sha256: `76058780514c22eb11a5c86c95ea5ce476a3bee270cdb3f651c56e30d95e1078`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260311_010225Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260311_010225Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "eb95a463ad6e96f2da233e9cee5501dce62974268aed3648f89c4900681aa575",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260311_010225Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203461,
    "items_db": 203493,
    "items_missing_in_db": 28,
    "codes_upstream": 83933,
    "codes_db": 243799,
    "codes_missing_in_db": 10,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "89ed4f79d1095d8bf52ef140934616a322a0ec1db326fbc3eeae7ddb43a73f44",
  "csv_size_bytes": 26066472,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260311_010225Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203461,
  "items_db": 203493,
  "items_missing_in_db": 28,
  "codes_upstream": 83933,
  "codes_db": 243799,
  "codes_missing_in_db": 10,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 28,
  "db_inserted_codes": 10
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243837,
  "distinct_bl_part_id": 169235,
  "null_boid": 165670,
  "null_weight": 90019,
  "null_bk_part_id": 38,
  "null_bk_part_key": 38,
  "null_api_item_type": 38,
  "null_brikick_name": 38,
  "null_part_name": 90116,
  "null_element_id": 160600,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165670`
- null_weight: `90019`
- corruption_pattern_count: `0`
