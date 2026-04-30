# Brikick DB Post-Update Report

- created_at_utc: `20260430_015315Z`
- db_path: `database/brickovery.db`
- db_sha256: `fd7fdf0d25d4ab373bb563962d1dee7e9277b7fad577036a390bff74022973a3`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260430_015305Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260430_015305Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "402b482060e19c40d6ddf0b46c0b8a813ec9db8df0f04c6b5400a48dfa53a186",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260430_015305Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205389,
    "items_db": 205747,
    "items_missing_in_db": 16,
    "codes_upstream": 84461,
    "codes_db": 246448,
    "codes_missing_in_db": 134,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "014bd312a50b3c2c15f5f3d6416f6dbb160e1e270e86174058f90821743b545c",
  "csv_size_bytes": 26215928,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260430_015305Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205389,
  "items_db": 205747,
  "items_missing_in_db": 16,
  "codes_upstream": 84461,
  "codes_db": 246448,
  "codes_missing_in_db": 134,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 16,
  "db_inserted_codes": 134
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246598,
  "distinct_bl_part_id": 171375,
  "null_boid": 168424,
  "null_weight": 92601,
  "null_bk_part_id": 150,
  "null_bk_part_key": 150,
  "null_api_item_type": 150,
  "null_brikick_name": 150,
  "null_part_name": 92877,
  "null_element_id": 163361,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168424`
- null_weight: `92601`
- corruption_pattern_count: `0`
