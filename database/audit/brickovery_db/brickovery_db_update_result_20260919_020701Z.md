# Brikick DB Post-Update Report

- created_at_utc: `20260919_020701Z`
- db_path: `database/brickovery.db`
- db_sha256: `b642b05cad199bc57996a520f93d2b8f35de76344c96321c3f814dba8da5d03c`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260919_020649Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260919_020649Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "46d69c6473685a73d87686c295d18316367128101b208150e9ed388d562158b1",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260919_020649Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210788,
    "items_db": 211653,
    "items_missing_in_db": 3,
    "codes_upstream": 86703,
    "codes_db": 255648,
    "codes_missing_in_db": 15,
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
  "csv_sha256": "56cd5d557dd71c32ec0620b62cb936085d04d3d9fbcb629bbb38a440fb89db1a",
  "csv_size_bytes": 26744934,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260919_020649Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210788,
  "items_db": 211653,
  "items_missing_in_db": 3,
  "codes_upstream": 86703,
  "codes_db": 255648,
  "codes_missing_in_db": 15,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 3,
  "db_inserted_codes": 15
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255666,
  "distinct_bl_part_id": 176468,
  "null_boid": 177489,
  "null_weight": 100370,
  "null_bk_part_id": 18,
  "null_bk_part_key": 18,
  "null_api_item_type": 18,
  "null_brikick_name": 18,
  "null_part_name": 101945,
  "null_element_id": 172429,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177489`
- null_weight: `100370`
- corruption_pattern_count: `0`
