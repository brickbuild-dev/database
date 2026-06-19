# Brikick DB Post-Update Report

- created_at_utc: `20260619_025313Z`
- db_path: `database/brickovery.db`
- db_sha256: `e26b74f54f32a90b34149cda1989ff985b211dec0d1ff35f534ce78e63df65cb`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260619_025302Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260619_025302Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "55edc45be8a3daf8f92f054e4497801d33867466066d75a3a92a129ac1b6cdde",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260619_025302Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207265,
    "items_db": 207883,
    "items_missing_in_db": 13,
    "codes_upstream": 84899,
    "codes_db": 250002,
    "codes_missing_in_db": 4,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "e8bc234cbccdc28832720ea19ff9a5b4c526dffc4c13f2800193973d1277a959",
  "csv_size_bytes": 26420659,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260619_025302Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207265,
  "items_db": 207883,
  "items_missing_in_db": 13,
  "codes_upstream": 84899,
  "codes_db": 250002,
  "codes_missing_in_db": 4,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 13,
  "db_inserted_codes": 3
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250018,
  "distinct_bl_part_id": 173153,
  "null_boid": 171842,
  "null_weight": 95353,
  "null_bk_part_id": 16,
  "null_bk_part_key": 16,
  "null_api_item_type": 16,
  "null_brikick_name": 16,
  "null_part_name": 96297,
  "null_element_id": 166781,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171842`
- null_weight: `95353`
- corruption_pattern_count: `0`
