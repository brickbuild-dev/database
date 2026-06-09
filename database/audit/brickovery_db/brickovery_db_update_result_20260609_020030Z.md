# Brikick DB Post-Update Report

- created_at_utc: `20260609_020030Z`
- db_path: `database/brickovery.db`
- db_sha256: `0e645dd6b1a9388faace2b2c7cdedc7bb95c6166bca487a76a0f44d38b3932a8`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260609_020018Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260609_020018Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "dcd058f0869a6548f744661382e93ad58654985267f85350893768f1b9da8a27",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260609_020018Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 206671,
    "items_db": 207232,
    "items_missing_in_db": 36,
    "codes_upstream": 84592,
    "codes_db": 249051,
    "codes_missing_in_db": 23,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "e5c92a4a5d391fb0a76da6e7d924de6f52ba179981c83dd783b6a7fe97e4d3e2",
  "csv_size_bytes": 26366801,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260609_020018Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 206671,
  "items_db": 207232,
  "items_missing_in_db": 36,
  "codes_upstream": 84592,
  "codes_db": 249051,
  "codes_missing_in_db": 23,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 36,
  "db_inserted_codes": 18
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 249105,
  "distinct_bl_part_id": 172529,
  "null_boid": 170930,
  "null_weight": 94483,
  "null_bk_part_id": 54,
  "null_bk_part_key": 54,
  "null_api_item_type": 54,
  "null_brikick_name": 54,
  "null_part_name": 95384,
  "null_element_id": 165868,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `170930`
- null_weight: `94483`
- corruption_pattern_count: `0`
