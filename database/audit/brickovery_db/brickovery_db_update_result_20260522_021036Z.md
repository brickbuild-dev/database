# Brikick DB Post-Update Report

- created_at_utc: `20260522_021036Z`
- db_path: `database/brickovery.db`
- db_sha256: `762d2fe864bfec1aedbbab97deb0ec121a24c916756a8e61b8d10fd5a779d1e4`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260522_021026Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260522_021026Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "dc67d31b9b976c54d9cd8e7f701abff0c9e15bfeb82c2f4eff7a768f40dd6706",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260522_021026Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205915,
    "items_db": 206432,
    "items_missing_in_db": 20,
    "codes_upstream": 84398,
    "codes_db": 248072,
    "codes_missing_in_db": 23,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "9c15c4ef1d3499a76c484b830ae14d8133a441c0e653bad3fd11bc60f1fa4694",
  "csv_size_bytes": 26309634,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260522_021026Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205915,
  "items_db": 206432,
  "items_missing_in_db": 20,
  "codes_upstream": 84398,
  "codes_db": 248072,
  "codes_missing_in_db": 23,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 20,
  "db_inserted_codes": 23
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248115,
  "distinct_bl_part_id": 171978,
  "null_boid": 169940,
  "null_weight": 93554,
  "null_bk_part_id": 43,
  "null_bk_part_key": 43,
  "null_api_item_type": 43,
  "null_brikick_name": 43,
  "null_part_name": 94394,
  "null_element_id": 164878,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169940`
- null_weight: `93554`
- corruption_pattern_count: `0`
