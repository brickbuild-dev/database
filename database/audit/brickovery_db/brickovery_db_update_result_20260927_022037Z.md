# Brikick DB Post-Update Report

- created_at_utc: `20260927_022037Z`
- db_path: `database/brickovery.db`
- db_sha256: `077c4d4074383e6b7e6492456421bdb26ac0d9d0cd1072b91991189863cf4335`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260927_022025Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260927_022025Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "0fcb4035ca46ab811500f2aa36c14ee8c87814ae81eca322784cb0cc5f90576a",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260927_022025Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211161,
    "items_db": 212070,
    "items_missing_in_db": 7,
    "codes_upstream": 86710,
    "codes_db": 256087,
    "codes_missing_in_db": 2,
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
  "csv_sha256": "8aad07ba531f2f04b31f0560a473771c8ded51d8a60e1e0604e118a4d14fbef7",
  "csv_size_bytes": 26768228,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260927_022025Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211161,
  "items_db": 212070,
  "items_missing_in_db": 7,
  "codes_upstream": 86710,
  "codes_db": 256087,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 7,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 256096,
  "distinct_bl_part_id": 176874,
  "null_boid": 177917,
  "null_weight": 100785,
  "null_bk_part_id": 9,
  "null_bk_part_key": 9,
  "null_api_item_type": 9,
  "null_brikick_name": 9,
  "null_part_name": 102375,
  "null_element_id": 172859,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177917`
- null_weight: `100785`
- corruption_pattern_count: `0`
