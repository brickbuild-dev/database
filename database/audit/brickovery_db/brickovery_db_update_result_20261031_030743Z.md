# Brikick DB Post-Update Report

- created_at_utc: `20261031_030743Z`
- db_path: `database/brickovery.db`
- db_sha256: `c4709c7cf332b2ed5a4b351b46c289f61a35c13520c3c3b773dd6067f24b53cb`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261031_030733Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261031_030733Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "6185579734afd3a23cc96ad70287e80cc5bb375002c2b6e5026e5ca014524800",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261031_030733Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211992,
    "items_db": 213867,
    "items_missing_in_db": 2,
    "codes_upstream": 87125,
    "codes_db": 258660,
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
  "csv_sha256": "897303ee9bf8c242bd651cc115e38a395f07ebef15713dbfef4ab1a4b6dc42c9",
  "csv_size_bytes": 26917558,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261031_030733Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211992,
  "items_db": 213867,
  "items_missing_in_db": 2,
  "codes_upstream": 87125,
  "codes_db": 258660,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 2,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258662,
  "distinct_bl_part_id": 178585,
  "null_boid": 180482,
  "null_weight": 103216,
  "null_bk_part_id": 2,
  "null_bk_part_key": 2,
  "null_api_item_type": 2,
  "null_brikick_name": 2,
  "null_part_name": 104941,
  "null_element_id": 175425,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180482`
- null_weight: `103216`
- corruption_pattern_count: `0`
