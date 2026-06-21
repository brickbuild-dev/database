# Brikick DB Post-Update Report

- created_at_utc: `20260621_023710Z`
- db_path: `database/brickovery.db`
- db_sha256: `9f6c2c3a05eb98906ec6d3ffbff3aa426ac5d98038e7e2a52edd828d7972f8c1`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260621_023659Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260621_023659Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "6bf9eba38ed7b5f33943f1736d3044e9984b60bebe88d66d60b3f24ba11ca49b",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260621_023659Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207343,
    "items_db": 207958,
    "items_missing_in_db": 19,
    "codes_upstream": 84935,
    "codes_db": 250082,
    "codes_missing_in_db": 34,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "7a6839d333eabffcec77fb16abec61534607cf77ed9ba29364dcbbcd77175686",
  "csv_size_bytes": 26425168,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260621_023659Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207343,
  "items_db": 207958,
  "items_missing_in_db": 19,
  "codes_upstream": 84935,
  "codes_db": 250082,
  "codes_missing_in_db": 34,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 19,
  "db_inserted_codes": 34
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250135,
  "distinct_bl_part_id": 173232,
  "null_boid": 171959,
  "null_weight": 95469,
  "null_bk_part_id": 53,
  "null_bk_part_key": 53,
  "null_api_item_type": 53,
  "null_brikick_name": 53,
  "null_part_name": 96414,
  "null_element_id": 166898,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171959`
- null_weight: `95469`
- corruption_pattern_count: `0`
