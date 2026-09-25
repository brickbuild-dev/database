# Brikick DB Post-Update Report

- created_at_utc: `20260925_090541Z`
- db_path: `database/brickovery.db`
- db_sha256: `fd0c76cd8e6db51735d1defd2a37a512ebc2232f248a4bca01f5978f51c92552`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260925_090529Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260925_090529Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "252baf68c737f1a5590b31487fdf5f1062e3ae7c1ab0f68a35b595b883633c7b",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260925_090529Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211140,
    "items_db": 212053,
    "items_missing_in_db": 3,
    "codes_upstream": 86708,
    "codes_db": 256070,
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
  "csv_sha256": "a8b269ac48ab57e1a4026f95c10a9c12b4078f1e6a05b223b5256f50a950b16f",
  "csv_size_bytes": 26767302,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260925_090529Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211140,
  "items_db": 212053,
  "items_missing_in_db": 3,
  "codes_upstream": 86708,
  "codes_db": 256070,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 3,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 256073,
  "distinct_bl_part_id": 176854,
  "null_boid": 177894,
  "null_weight": 100762,
  "null_bk_part_id": 3,
  "null_bk_part_key": 3,
  "null_api_item_type": 3,
  "null_brikick_name": 3,
  "null_part_name": 102352,
  "null_element_id": 172836,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177894`
- null_weight: `100762`
- corruption_pattern_count: `0`
