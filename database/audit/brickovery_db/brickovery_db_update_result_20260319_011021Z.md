# Brikick DB Post-Update Report

- created_at_utc: `20260319_011021Z`
- db_path: `database/brickovery.db`
- db_sha256: `082b7878cd44658a753d12d318cfb923ad7f72f28d615dcce54ee6df68adfeee`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260319_011009Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260319_011009Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "6b900a42d45c376bc8687123a6d309fdd2241b5a43e1d43aba40a5061de61155",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260319_011009Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203693,
    "items_db": 203746,
    "items_missing_in_db": 22,
    "codes_upstream": 84011,
    "codes_db": 244135,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "d900cb0345ac669a2cc09233e253e1729a4cc70349bbf9b8af2a15d9f0736b44",
  "csv_size_bytes": 26085822,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260319_011009Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203693,
  "items_db": 203746,
  "items_missing_in_db": 22,
  "codes_upstream": 84011,
  "codes_db": 244135,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 22,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 244157,
  "distinct_bl_part_id": 169475,
  "null_boid": 165990,
  "null_weight": 90331,
  "null_bk_part_id": 22,
  "null_bk_part_key": 22,
  "null_api_item_type": 22,
  "null_brikick_name": 22,
  "null_part_name": 90436,
  "null_element_id": 160920,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165990`
- null_weight: `90331`
- corruption_pattern_count: `0`
