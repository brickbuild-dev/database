# Brikick DB Post-Update Report

- created_at_utc: `20260411_011705Z`
- db_path: `database/brickovery.db`
- db_sha256: `9601b30e57ee709269a6be3a3755511295d5c7671a7f00f54d7798ada7be9926`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260411_011654Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260411_011654Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "5847780c34370531903f2452a94d8ea0a94eac7aa6721ff26dce0222cf9d76eb",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260411_011654Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205173,
    "items_db": 205484,
    "items_missing_in_db": 24,
    "codes_upstream": 84139,
    "codes_db": 245976,
    "codes_missing_in_db": 7,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "0d36f6f726ecbcb37dc1cd75a7a561c3e6506755ae952e05a98e0db9663130c1",
  "csv_size_bytes": 26188774,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260411_011654Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205173,
  "items_db": 205484,
  "items_missing_in_db": 24,
  "codes_upstream": 84139,
  "codes_db": 245976,
  "codes_missing_in_db": 7,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 24,
  "db_inserted_codes": 7
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246007,
  "distinct_bl_part_id": 171154,
  "null_boid": 167837,
  "null_weight": 92151,
  "null_bk_part_id": 31,
  "null_bk_part_key": 31,
  "null_api_item_type": 31,
  "null_brikick_name": 31,
  "null_part_name": 92286,
  "null_element_id": 162770,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167837`
- null_weight: `92151`
- corruption_pattern_count: `0`
