# Brikick DB Post-Update Report

- created_at_utc: `20260824_004023Z`
- db_path: `database/brickovery.db`
- db_sha256: `5669a0cbb23e3d2f1f301468897ba70ca056b3ef6b8dbeeb609704eae0fdba04`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260824_004011Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260824_004011Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "03c67b6fee7e03576c4c8bfa18987851491ea5f49f1e61efe83fbc3d89d44e41",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260824_004011Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209789,
    "items_db": 210577,
    "items_missing_in_db": 10,
    "codes_upstream": 86311,
    "codes_db": 254136,
    "codes_missing_in_db": 8,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "8cce1ff9345eb498bf3408952f459e08081567989125b74d0644655b15b56934",
  "csv_size_bytes": 26656864,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260824_004011Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209789,
  "items_db": 210577,
  "items_missing_in_db": 10,
  "codes_upstream": 86311,
  "codes_db": 254136,
  "codes_missing_in_db": 8,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 10,
  "db_inserted_codes": 8
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254154,
  "distinct_bl_part_id": 175631,
  "null_boid": 175977,
  "null_weight": 98954,
  "null_bk_part_id": 18,
  "null_bk_part_key": 18,
  "null_api_item_type": 18,
  "null_brikick_name": 18,
  "null_part_name": 100433,
  "null_element_id": 170917,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175977`
- null_weight: `98954`
- corruption_pattern_count: `0`
