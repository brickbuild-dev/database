# Brikick DB Post-Update Report

- created_at_utc: `20261002_170622Z`
- db_path: `database/brickovery.db`
- db_sha256: `5e99a88ac12d5dc67e227dbc87024b53d5f1e2f68b402cd343ae1558bba7b701`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261002_170609Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261002_170609Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "824e032a072ebb92710e988fd042e67844ea05cfc6db1e6a5f85423a37b00ff9",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261002_170609Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211400,
    "items_db": 213221,
    "items_missing_in_db": 15,
    "codes_upstream": 86746,
    "codes_db": 257642,
    "codes_missing_in_db": 0,
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
  "csv_sha256": "ab424050bdc5618838a708e0abfffc72eb552043c85c0721a22f48b361cb004c",
  "csv_size_bytes": 26858789,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261002_170609Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211400,
  "items_db": 213221,
  "items_missing_in_db": 15,
  "codes_upstream": 86746,
  "codes_db": 257642,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 15,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 257657,
  "distinct_bl_part_id": 177987,
  "null_boid": 179478,
  "null_weight": 102329,
  "null_bk_part_id": 15,
  "null_bk_part_key": 15,
  "null_api_item_type": 15,
  "null_brikick_name": 15,
  "null_part_name": 103936,
  "null_element_id": 174420,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179478`
- null_weight: `102329`
- corruption_pattern_count: `0`
