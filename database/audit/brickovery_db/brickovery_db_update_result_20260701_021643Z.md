# Brikick DB Post-Update Report

- created_at_utc: `20260701_021643Z`
- db_path: `database/brickovery.db`
- db_sha256: `d1e640b47ea6ae1e15174b961872364ca685f0e21008741b0ea959e78f1d940f`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260701_021632Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260701_021632Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "ab70e19a4c0bd5b1797e35e03eab92a27e3d305f7f5d80634e9094c4a54e336c",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260701_021632Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207603,
    "items_db": 208235,
    "items_missing_in_db": 44,
    "codes_upstream": 85136,
    "codes_db": 250595,
    "codes_missing_in_db": 17,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "47738856d0822bf2bb493904969eebf5862b1b5cc13bfacc529cdb3d4648d8fc",
  "csv_size_bytes": 26455186,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260701_021632Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207603,
  "items_db": 208235,
  "items_missing_in_db": 44,
  "codes_upstream": 85136,
  "codes_db": 250595,
  "codes_missing_in_db": 17,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 44,
  "db_inserted_codes": 16
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250655,
  "distinct_bl_part_id": 173525,
  "null_boid": 172479,
  "null_weight": 95930,
  "null_bk_part_id": 60,
  "null_bk_part_key": 60,
  "null_api_item_type": 60,
  "null_brikick_name": 60,
  "null_part_name": 96934,
  "null_element_id": 167418,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172479`
- null_weight: `95930`
- corruption_pattern_count: `0`
