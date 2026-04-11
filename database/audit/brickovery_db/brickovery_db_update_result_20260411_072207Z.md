# Brikick DB Post-Update Report

- created_at_utc: `20260411_072207Z`
- db_path: `database/brickovery.db`
- db_sha256: `9e0c926f637670a444c38c76d54e4ef983abdc2e4d7b51be92bfcbf3542deaff`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260411_072156Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260411_072156Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "432d2f194ceb0e7b735490b8eafd00ee084540f868cb3a80b4a77f264f869eb3",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260411_072156Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205173,
    "items_db": 205508,
    "items_missing_in_db": 2,
    "codes_upstream": 84139,
    "codes_db": 246007,
    "codes_missing_in_db": 5,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "e3d002b7653e5223ccaf91e4a56c201ec93a11f304082dda45d1ef72f2351fa1",
  "csv_size_bytes": 26190588,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260411_072156Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205173,
  "items_db": 205508,
  "items_missing_in_db": 2,
  "codes_upstream": 84139,
  "codes_db": 246007,
  "codes_missing_in_db": 5,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 2,
  "db_inserted_codes": 5
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246014,
  "distinct_bl_part_id": 171156,
  "null_boid": 167844,
  "null_weight": 92153,
  "null_bk_part_id": 7,
  "null_bk_part_key": 7,
  "null_api_item_type": 7,
  "null_brikick_name": 7,
  "null_part_name": 92293,
  "null_element_id": 162777,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167844`
- null_weight: `92153`
- corruption_pattern_count: `0`
