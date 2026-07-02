# Brikick DB Post-Update Report

- created_at_utc: `20260702_020919Z`
- db_path: `database/brickovery.db`
- db_sha256: `ed20495613cfef8c37acbbb160d5375baafb6411736e30e24ed40aa96dae1d74`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260702_020908Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260702_020908Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "dd01d2ad1fa1beaf46632f48ec5a1a0cfe97955f59dd72a54d4393af4aaddc76",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260702_020908Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207647,
    "items_db": 208279,
    "items_missing_in_db": 46,
    "codes_upstream": 85164,
    "codes_db": 250655,
    "codes_missing_in_db": 28,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "9357d62cd7d34b1edcac7b60fc4bda61ea8c887d3e973c32d5876c4aed191004",
  "csv_size_bytes": 26458656,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260702_020908Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207647,
  "items_db": 208279,
  "items_missing_in_db": 46,
  "codes_upstream": 85164,
  "codes_db": 250655,
  "codes_missing_in_db": 28,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 46,
  "db_inserted_codes": 28
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250729,
  "distinct_bl_part_id": 173559,
  "null_boid": 172553,
  "null_weight": 96004,
  "null_bk_part_id": 74,
  "null_bk_part_key": 74,
  "null_api_item_type": 74,
  "null_brikick_name": 74,
  "null_part_name": 97008,
  "null_element_id": 167492,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172553`
- null_weight: `96004`
- corruption_pattern_count: `0`
