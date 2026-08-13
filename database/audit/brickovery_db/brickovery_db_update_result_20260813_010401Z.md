# Brikick DB Post-Update Report

- created_at_utc: `20260813_010401Z`
- db_path: `database/brickovery.db`
- db_sha256: `8c3242ad79b37e27f8406fe0f5cf1d6f57973850e0d47859ff68782239d06f19`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260813_010349Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260813_010349Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "96659ec066fadc6748396c29ffad00b014e9e3b73bb3a131bb531c61206c95d1",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260813_010349Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209554,
    "items_db": 210262,
    "items_missing_in_db": 72,
    "codes_upstream": 86126,
    "codes_db": 253593,
    "codes_missing_in_db": 55,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "4a8ed236ae00a183c210577018e445741b3b463e6ee38b39d6c259a74e4b7686",
  "csv_size_bytes": 26625139,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260813_010349Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209554,
  "items_db": 210262,
  "items_missing_in_db": 72,
  "codes_upstream": 86126,
  "codes_db": 253593,
  "codes_missing_in_db": 55,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 72,
  "db_inserted_codes": 51
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253716,
  "distinct_bl_part_id": 175382,
  "null_boid": 175539,
  "null_weight": 98522,
  "null_bk_part_id": 123,
  "null_bk_part_key": 123,
  "null_api_item_type": 123,
  "null_brikick_name": 123,
  "null_part_name": 99995,
  "null_element_id": 170479,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175539`
- null_weight: `98522`
- corruption_pattern_count: `0`
