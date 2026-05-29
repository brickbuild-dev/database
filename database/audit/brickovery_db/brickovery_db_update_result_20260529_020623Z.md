# Brikick DB Post-Update Report

- created_at_utc: `20260529_020623Z`
- db_path: `database/brickovery.db`
- db_sha256: `e586300fce2f74afa4eaa114c1d32834fc0c2d434f9dd933b2516e4ab331e575`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260529_020612Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260529_020612Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "cf663bb6c3faed96bd35bb9682171d6a112c0c491ca8f783d91b6d47bf6a8ee2",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260529_020612Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205959,
    "items_db": 206519,
    "items_missing_in_db": 13,
    "codes_upstream": 84410,
    "codes_db": 248193,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "3c3a122842a1557b3cfcceee5d78bea646dc3f37ac83eafd2fb9c2772dce5d83",
  "csv_size_bytes": 26316769,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260529_020612Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205959,
  "items_db": 206519,
  "items_missing_in_db": 13,
  "codes_upstream": 84410,
  "codes_db": 248193,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 13,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248206,
  "distinct_bl_part_id": 172048,
  "null_boid": 170031,
  "null_weight": 93643,
  "null_bk_part_id": 13,
  "null_bk_part_key": 13,
  "null_api_item_type": 13,
  "null_brikick_name": 13,
  "null_part_name": 94485,
  "null_element_id": 164969,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `170031`
- null_weight: `93643`
- corruption_pattern_count: `0`
