# Brikick DB Post-Update Report

- created_at_utc: `20260611_023753Z`
- db_path: `database/brickovery.db`
- db_sha256: `04f4aa508b4cb7e7062e3a5c03be4f874948316acc2bd738e8450d7b6b84270d`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260611_023742Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260611_023742Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "f7b0cab98a9dd7d8aa085435a0d312f50b568cfa209d2e2348af666f178306e8",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260611_023742Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 206710,
    "items_db": 207285,
    "items_missing_in_db": 24,
    "codes_upstream": 84665,
    "codes_db": 249167,
    "codes_missing_in_db": 26,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "f27141dda6f76f915ecbc41177bc4abcf506649f84adef34bf24f4a0c471341d",
  "csv_size_bytes": 26373341,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260611_023742Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 206710,
  "items_db": 207285,
  "items_missing_in_db": 24,
  "codes_upstream": 84665,
  "codes_db": 249167,
  "codes_missing_in_db": 26,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 24,
  "db_inserted_codes": 23
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 249214,
  "distinct_bl_part_id": 172570,
  "null_boid": 171039,
  "null_weight": 94569,
  "null_bk_part_id": 47,
  "null_bk_part_key": 47,
  "null_api_item_type": 47,
  "null_brikick_name": 47,
  "null_part_name": 95493,
  "null_element_id": 165977,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171039`
- null_weight: `94569`
- corruption_pattern_count: `0`
