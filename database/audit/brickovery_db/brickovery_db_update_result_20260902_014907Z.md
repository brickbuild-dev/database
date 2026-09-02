# Brikick DB Post-Update Report

- created_at_utc: `20260902_014907Z`
- db_path: `database/brickovery.db`
- db_sha256: `76de25b6d1ac1b96f49c68d20ce8e84a0fc8ded827e1d99b04c451c71b24e8bb`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260902_014856Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260902_014856Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "9a75658db54f2f19fd800d6605928bc9531e7347e159a079014493ae45ec004c",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260902_014856Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210129,
    "items_db": 210745,
    "items_missing_in_db": 205,
    "codes_upstream": 86366,
    "codes_db": 254400,
    "codes_missing_in_db": 10,
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
  "csv_sha256": "268eae1b2c5ad92e97f76f2090dd938d4c3546f5a9d7c7df2ee7a4802e3da73f",
  "csv_size_bytes": 26672314,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260902_014856Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210129,
  "items_db": 210745,
  "items_missing_in_db": 205,
  "codes_upstream": 86366,
  "codes_db": 254400,
  "codes_missing_in_db": 10,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 205,
  "db_inserted_codes": 5
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254610,
  "distinct_bl_part_id": 175866,
  "null_boid": 176433,
  "null_weight": 99387,
  "null_bk_part_id": 210,
  "null_bk_part_key": 210,
  "null_api_item_type": 210,
  "null_brikick_name": 210,
  "null_part_name": 100889,
  "null_element_id": 171373,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176433`
- null_weight: `99387`
- corruption_pattern_count: `0`
