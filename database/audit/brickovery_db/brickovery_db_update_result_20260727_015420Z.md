# Brikick DB Post-Update Report

- created_at_utc: `20260727_015420Z`
- db_path: `database/brickovery.db`
- db_sha256: `e5f0db743fb6a7d577e6f094dda4302352cea51778903e9171ca26fe574e666e`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260727_015409Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260727_015409Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "a872fd877049c217f0b32c238ce82c24605f4050879989cab92668eb7fa264af",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260727_015409Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 208104,
    "items_db": 208808,
    "items_missing_in_db": 22,
    "codes_upstream": 85416,
    "codes_db": 251455,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "dc9d83bc1bd9dac6efd6390c1f1535af1b7c6facf8b4efc72380ba7c140f3f32",
  "csv_size_bytes": 26504258,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260727_015409Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 208104,
  "items_db": 208808,
  "items_missing_in_db": 22,
  "codes_upstream": 85416,
  "codes_db": 251455,
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
  "brickovery_db_rows": 251477,
  "distinct_bl_part_id": 174046,
  "null_boid": 173301,
  "null_weight": 96641,
  "null_bk_part_id": 22,
  "null_bk_part_key": 22,
  "null_api_item_type": 22,
  "null_brikick_name": 22,
  "null_part_name": 97756,
  "null_element_id": 168240,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `173301`
- null_weight: `96641`
- corruption_pattern_count: `0`
