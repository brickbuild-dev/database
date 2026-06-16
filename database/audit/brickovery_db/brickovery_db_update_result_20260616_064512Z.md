# Brikick DB Post-Update Report

- created_at_utc: `20260616_064512Z`
- db_path: `database/brickovery.db`
- db_sha256: `48a694ebc3573c946b3a850ccb731cf1940d6ff77573b524ac2b7134e09718a1`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260616_064504Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260616_064504Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "78ea58d52418d5273d803ae46cbdb19a2cfd50a2f18913e3e596490e030a46d2",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260616_064504Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207205,
    "items_db": 207821,
    "items_missing_in_db": 1,
    "codes_upstream": 84851,
    "codes_db": 249897,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "8fa90f676fddec4455153912f7483425f366c83e33ddd096f4815d1581a204f7",
  "csv_size_bytes": 26414504,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260616_064504Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207205,
  "items_db": 207821,
  "items_missing_in_db": 1,
  "codes_upstream": 84851,
  "codes_db": 249897,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 1,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 249898,
  "distinct_bl_part_id": 173081,
  "null_boid": 171722,
  "null_weight": 95238,
  "null_bk_part_id": 1,
  "null_bk_part_key": 1,
  "null_api_item_type": 1,
  "null_brikick_name": 1,
  "null_part_name": 96177,
  "null_element_id": 166661,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171722`
- null_weight: `95238`
- corruption_pattern_count: `0`
