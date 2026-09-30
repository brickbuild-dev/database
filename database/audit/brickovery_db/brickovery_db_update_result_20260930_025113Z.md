# Brikick DB Post-Update Report

- created_at_utc: `20260930_025113Z`
- db_path: `database/brickovery.db`
- db_sha256: `3127e2bb6250c42470931c602aa84deef7f22a81daf3d3ddef6145c3f361ae40`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260930_025102Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260930_025102Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "519b654664d2275a88ed7196fdae8506ee5691b886ad8afec8d14575e3cda839",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260930_025102Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211271,
    "items_db": 212169,
    "items_missing_in_db": 938,
    "codes_upstream": 86725,
    "codes_db": 256198,
    "codes_missing_in_db": 373,
    "unknown_color_tokens": [
      "Royal Blue",
      "Speckle Copper",
      "Speckle Gold",
      "Speckle Silver"
    ],
    "unknown_color_tokens_count": 4,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "d5187c870647717f1173508f98ce600c1abc997318c2b9689616ddfc536b8d65",
  "csv_size_bytes": 26774230,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260930_025102Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211271,
  "items_db": 212169,
  "items_missing_in_db": 938,
  "codes_upstream": 86725,
  "codes_db": 256198,
  "codes_missing_in_db": 373,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 938,
  "db_inserted_codes": 373
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 257509,
  "distinct_bl_part_id": 177899,
  "null_boid": 179330,
  "null_weight": 102190,
  "null_bk_part_id": 1311,
  "null_bk_part_key": 1311,
  "null_api_item_type": 1311,
  "null_brikick_name": 1311,
  "null_part_name": 103788,
  "null_element_id": 174272,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179330`
- null_weight: `102190`
- corruption_pattern_count: `0`
