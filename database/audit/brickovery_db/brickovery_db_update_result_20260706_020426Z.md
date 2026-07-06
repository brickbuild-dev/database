# Brikick DB Post-Update Report

- created_at_utc: `20260706_020426Z`
- db_path: `database/brickovery.db`
- db_sha256: `e094fa5a61e7ea20070ced36e35a2d04b67d928222cb00f9dc56f79a78d2270f`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260706_020415Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260706_020415Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "8fa272dd34565fb02287d9493154f078551a14ef36a4f8d716232491e19c1d3b",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260706_020415Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207737,
    "items_db": 208400,
    "items_missing_in_db": 15,
    "codes_upstream": 85214,
    "codes_db": 250843,
    "codes_missing_in_db": 10,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "39ce8c3a0a127e9fdbb22bace39a67fb22b95038e8a26a01b7953721f794c205",
  "csv_size_bytes": 26469615,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260706_020415Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207737,
  "items_db": 208400,
  "items_missing_in_db": 15,
  "codes_upstream": 85214,
  "codes_db": 250843,
  "codes_missing_in_db": 10,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 15,
  "db_inserted_codes": 10
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250868,
  "distinct_bl_part_id": 173638,
  "null_boid": 172692,
  "null_weight": 96142,
  "null_bk_part_id": 25,
  "null_bk_part_key": 25,
  "null_api_item_type": 25,
  "null_brikick_name": 25,
  "null_part_name": 97147,
  "null_element_id": 167631,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172692`
- null_weight: `96142`
- corruption_pattern_count: `0`
