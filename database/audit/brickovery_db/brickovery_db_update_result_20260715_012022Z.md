# Brikick DB Post-Update Report

- created_at_utc: `20260715_012022Z`
- db_path: `database/brickovery.db`
- db_sha256: `3606df669cf075fc441b317c25e64d0f4227922d9c4042676c47fae3c509aea7`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260715_012011Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260715_012011Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "03237635b0eb77ecb78a1c1f12677d7e8c35f0f3431fefe965f04389ca4a2a9a",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260715_012011Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207860,
    "items_db": 208534,
    "items_missing_in_db": 17,
    "codes_upstream": 85364,
    "codes_db": 251132,
    "codes_missing_in_db": 2,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "a7cc52e109be7ac53b0ee53ff9f0d6997534c3e50de1504a61c37f007ebb5340",
  "csv_size_bytes": 26486284,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260715_012011Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207860,
  "items_db": 208534,
  "items_missing_in_db": 17,
  "codes_upstream": 85364,
  "codes_db": 251132,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 17,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251151,
  "distinct_bl_part_id": 173771,
  "null_boid": 172975,
  "null_weight": 96322,
  "null_bk_part_id": 19,
  "null_bk_part_key": 19,
  "null_api_item_type": 19,
  "null_brikick_name": 19,
  "null_part_name": 97430,
  "null_element_id": 167914,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172975`
- null_weight: `96322`
- corruption_pattern_count: `0`
