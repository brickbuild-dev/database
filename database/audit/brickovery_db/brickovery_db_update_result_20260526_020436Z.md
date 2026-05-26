# Brikick DB Post-Update Report

- created_at_utc: `20260526_020436Z`
- db_path: `database/brickovery.db`
- db_sha256: `ca7be0981535fc1696d8df9b58f39faa47000925879d744016fd85c60bca79d8`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260526_020425Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260526_020425Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "2e712639e80d836c1dcb8b3c106eea40e69a09cb5b679315a9ef023f561c8f07",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260526_020425Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205935,
    "items_db": 206493,
    "items_missing_in_db": 7,
    "codes_upstream": 84409,
    "codes_db": 248166,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "be194f2cc8e14122cdb3b429b00b7b4b7901823037db5edc13dc322f4981098f",
  "csv_size_bytes": 26315138,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260526_020425Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205935,
  "items_db": 206493,
  "items_missing_in_db": 7,
  "codes_upstream": 84409,
  "codes_db": 248166,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 7,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248173,
  "distinct_bl_part_id": 172021,
  "null_boid": 169998,
  "null_weight": 93610,
  "null_bk_part_id": 7,
  "null_bk_part_key": 7,
  "null_api_item_type": 7,
  "null_brikick_name": 7,
  "null_part_name": 94452,
  "null_element_id": 164936,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169998`
- null_weight: `93610`
- corruption_pattern_count: `0`
