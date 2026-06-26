# Brikick DB Post-Update Report

- created_at_utc: `20260626_021218Z`
- db_path: `database/brickovery.db`
- db_sha256: `32cf55fc95279cea4da24eb8095960f6a9cccdc553e4f87851be56f5260720ef`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260626_021206Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260626_021206Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "6bd353c5dc40307d39c33e24ea23fc0911957f39f7984a4e2baff14d0fa3213e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260626_021206Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207520,
    "items_db": 208109,
    "items_missing_in_db": 73,
    "codes_upstream": 85027,
    "codes_db": 250317,
    "codes_missing_in_db": 62,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "d3cf64eccd314ca2ecea8d259378aa1aebaff1a4b56696c062fb5cce2c4a7481",
  "csv_size_bytes": 26438979,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260626_021206Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207520,
  "items_db": 208109,
  "items_missing_in_db": 73,
  "codes_upstream": 85027,
  "codes_db": 250317,
  "codes_missing_in_db": 62,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 73,
  "db_inserted_codes": 60
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250450,
  "distinct_bl_part_id": 173430,
  "null_boid": 172274,
  "null_weight": 95780,
  "null_bk_part_id": 133,
  "null_bk_part_key": 133,
  "null_api_item_type": 133,
  "null_brikick_name": 133,
  "null_part_name": 96729,
  "null_element_id": 167213,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172274`
- null_weight: `95780`
- corruption_pattern_count: `0`
