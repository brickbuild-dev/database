# Brikick DB Post-Update Report

- created_at_utc: `20260309_010715Z`
- db_path: `database/brickovery.db`
- db_sha256: `3027923bdb005d3b5a29ae383115450c250ac3cff78361f6505afa5ae97416f0`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260309_010703Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260309_010703Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "52e38272125547fda8e251903410a9bbfb730467d55853b577c452a00899b9df",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260309_010703Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203425,
    "items_db": 203445,
    "items_missing_in_db": 38,
    "codes_upstream": 83912,
    "codes_db": 243694,
    "codes_missing_in_db": 50,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "3fdba45e554353cb8ae0d8e33602554c0b74f6367a71b97bacbcd9388654a620",
  "csv_size_bytes": 26060391,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260309_010703Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203425,
  "items_db": 203445,
  "items_missing_in_db": 38,
  "codes_upstream": 83912,
  "codes_db": 243694,
  "codes_missing_in_db": 50,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 38,
  "db_inserted_codes": 49
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243781,
  "distinct_bl_part_id": 169199,
  "null_boid": 165614,
  "null_weight": 89971,
  "null_bk_part_id": 87,
  "null_bk_part_key": 87,
  "null_api_item_type": 87,
  "null_brikick_name": 87,
  "null_part_name": 90060,
  "null_element_id": 160544,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165614`
- null_weight: `89971`
- corruption_pattern_count: `0`
