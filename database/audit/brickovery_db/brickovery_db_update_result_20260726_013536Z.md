# Brikick DB Post-Update Report

- created_at_utc: `20260726_013536Z`
- db_path: `database/brickovery.db`
- db_sha256: `a1fc67333bebd3f90b42fa15f465cb537741eeb3461e50ee10a6243806f120b4`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260726_013524Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260726_013524Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "5528d8ed34a8792596d91689ddc1f49621b775fee22bc64398c930e5956c5793",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260726_013524Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 208102,
    "items_db": 208762,
    "items_missing_in_db": 46,
    "codes_upstream": 85415,
    "codes_db": 251401,
    "codes_missing_in_db": 10,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "33704cff15adf56d016b1b251311598ac4e2125299076d4d480cc92253946234",
  "csv_size_bytes": 26501510,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260726_013524Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 208102,
  "items_db": 208762,
  "items_missing_in_db": 46,
  "codes_upstream": 85415,
  "codes_db": 251401,
  "codes_missing_in_db": 10,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 46,
  "db_inserted_codes": 8
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251455,
  "distinct_bl_part_id": 174024,
  "null_boid": 173279,
  "null_weight": 96626,
  "null_bk_part_id": 54,
  "null_bk_part_key": 54,
  "null_api_item_type": 54,
  "null_brikick_name": 54,
  "null_part_name": 97734,
  "null_element_id": 168218,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `173279`
- null_weight: `96626`
- corruption_pattern_count: `0`
