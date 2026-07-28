# Brikick DB Post-Update Report

- created_at_utc: `20260728_012746Z`
- db_path: `database/brickovery.db`
- db_sha256: `fc269548070a327b3a845e311131465bd26c53977e88420e578ad1e051f6dcfd`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260728_012734Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260728_012734Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "75dfbbcbb95d7851896ff25d62bbdf0b8bb8fa1dfec1193513617681e40f3ca3",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260728_012734Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 208121,
    "items_db": 208830,
    "items_missing_in_db": 17,
    "codes_upstream": 85417,
    "codes_db": 251477,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "96406e1bff92968594e70470d6baa8c4df93974e31d297742c695d3b15977589",
  "csv_size_bytes": 26505428,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260728_012734Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 208121,
  "items_db": 208830,
  "items_missing_in_db": 17,
  "codes_upstream": 85417,
  "codes_db": 251477,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 17,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251495,
  "distinct_bl_part_id": 174063,
  "null_boid": 173319,
  "null_weight": 96659,
  "null_bk_part_id": 18,
  "null_bk_part_key": 18,
  "null_api_item_type": 18,
  "null_brikick_name": 18,
  "null_part_name": 97774,
  "null_element_id": 168258,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `173319`
- null_weight: `96659`
- corruption_pattern_count: `0`
