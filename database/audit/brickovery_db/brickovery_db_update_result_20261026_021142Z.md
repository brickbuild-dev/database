# Brikick DB Post-Update Report

- created_at_utc: `20261026_021142Z`
- db_path: `database/brickovery.db`
- db_sha256: `6c1e07d8ba5d179b1908b28fe30e3dbb03437824d6a4fe671e3b86bc8323068a`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261026_021130Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261026_021130Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "7f7a21fe84f2b948fda20791b82f46c115b407c35608687caf106411d0a1715b",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261026_021130Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211828,
    "items_db": 213660,
    "items_missing_in_db": 36,
    "codes_upstream": 87064,
    "codes_db": 258381,
    "codes_missing_in_db": 14,
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
  "csv_sha256": "e391db2c8fa3c7d9071a697f81d3f577f673f0780f6abe84dd8986481d884fda",
  "csv_size_bytes": 26901656,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261026_021130Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211828,
  "items_db": 213660,
  "items_missing_in_db": 36,
  "codes_upstream": 87064,
  "codes_db": 258381,
  "codes_missing_in_db": 14,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 36,
  "db_inserted_codes": 14
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258431,
  "distinct_bl_part_id": 178423,
  "null_boid": 180251,
  "null_weight": 102992,
  "null_bk_part_id": 50,
  "null_bk_part_key": 50,
  "null_api_item_type": 50,
  "null_brikick_name": 50,
  "null_part_name": 104710,
  "null_element_id": 175194,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180251`
- null_weight: `102992`
- corruption_pattern_count: `0`
