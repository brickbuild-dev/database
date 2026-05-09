# Brikick DB Post-Update Report

- created_at_utc: `20260509_015227Z`
- db_path: `database/brickovery.db`
- db_sha256: `e3fd592e48ee0e57676a333e8b715d0dbbbe05a3885ec80faf90c2e425377ea1`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260509_015216Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260509_015216Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "d1bcbbedc2590e5d0c9981a53717995253d2d8061e5425404b28b0acf84fd026",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260509_015216Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205723,
    "items_db": 206137,
    "items_missing_in_db": 27,
    "codes_upstream": 84204,
    "codes_db": 247543,
    "codes_missing_in_db": 22,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "f693424b38988201fc989146b57e64399a9d391b3a07abd50b322da6ab9c8556",
  "csv_size_bytes": 26279329,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260509_015216Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205723,
  "items_db": 206137,
  "items_missing_in_db": 27,
  "codes_upstream": 84204,
  "codes_db": 247543,
  "codes_missing_in_db": 22,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 27,
  "db_inserted_codes": 22
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247592,
  "distinct_bl_part_id": 171700,
  "null_boid": 169418,
  "null_weight": 93106,
  "null_bk_part_id": 49,
  "null_bk_part_key": 49,
  "null_api_item_type": 49,
  "null_brikick_name": 49,
  "null_part_name": 93871,
  "null_element_id": 164355,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169418`
- null_weight: `93106`
- corruption_pattern_count: `0`
