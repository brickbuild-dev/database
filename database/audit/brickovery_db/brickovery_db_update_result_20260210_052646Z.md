# Brikick DB Post-Update Report

- created_at_utc: `20260210_052646Z`
- db_path: `database/brickovery.db`
- db_sha256: `a18a69688ff0391b7d5dc9eaebb903113fcc5bc1451a77df31e8398ff441f144`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260210_052635Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260210_052635Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "3af19026383314d208ea2f49c1be3af7a53b44a2133cfc5fc3c2b169b1bd4bab",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260210_052635Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202445,
    "items_db": 202439,
    "items_missing_in_db": 8,
    "codes_upstream": 83305,
    "codes_db": 242144,
    "codes_missing_in_db": 11,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "54a08c4a48d4efb688a4a8298c069beff95993775074e615945a77310a80624f",
  "csv_size_bytes": 25971356,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260210_052635Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202445,
  "items_db": 202439,
  "items_missing_in_db": 8,
  "codes_upstream": 83305,
  "codes_db": 242144,
  "codes_missing_in_db": 11,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 8,
  "db_inserted_codes": 10
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242162,
  "distinct_bl_part_id": 168298,
  "null_boid": 163996,
  "null_weight": 88686,
  "null_bk_part_id": 18,
  "null_bk_part_key": 18,
  "null_api_item_type": 18,
  "null_brikick_name": 18,
  "null_part_name": 88441,
  "null_element_id": 158925,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `163996`
- null_weight: `88686`
- corruption_pattern_count: `0`
