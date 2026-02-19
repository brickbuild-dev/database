# Brikick DB Post-Update Report

- created_at_utc: `20260219_051444Z`
- db_path: `database/brickovery.db`
- db_sha256: `9f4b11c304963747169a7e938a14920861e319bd04874cc0390dbc6ff2167a84`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260219_051433Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260219_051433Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "07272f6dce0f57ba63494f9e701d41fdc8c1830af70a996abcd93650d75889cd",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260219_051433Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202550,
    "items_db": 202531,
    "items_missing_in_db": 26,
    "codes_upstream": 83445,
    "codes_db": 242377,
    "codes_missing_in_db": 4,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "4623d1dae577cae4d8999238de4ed455b0b04d1f5aa7c429c92d2df4523c33a6",
  "csv_size_bytes": 25984792,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260219_051433Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202550,
  "items_db": 202531,
  "items_missing_in_db": 26,
  "codes_upstream": 83445,
  "codes_db": 242377,
  "codes_missing_in_db": 4,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 26,
  "db_inserted_codes": 4
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242407,
  "distinct_bl_part_id": 168399,
  "null_boid": 164240,
  "null_weight": 88811,
  "null_bk_part_id": 30,
  "null_bk_part_key": 30,
  "null_api_item_type": 30,
  "null_brikick_name": 30,
  "null_part_name": 88686,
  "null_element_id": 159170,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `164240`
- null_weight: `88811`
- corruption_pattern_count: `0`
