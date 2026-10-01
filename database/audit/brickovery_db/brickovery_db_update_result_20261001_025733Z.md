# Brikick DB Post-Update Report

- created_at_utc: `20261001_025733Z`
- db_path: `database/brickovery.db`
- db_sha256: `5462e1135b2e718dffcc6a12c87175bbd855d45116cb83eb34b9a3fb2d295288`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261001_025721Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261001_025721Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "c7febffaecadac08584a7c30adbb99e57ba20844897def3ba4b82fdc8d987b52",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261001_025721Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211286,
    "items_db": 213107,
    "items_missing_in_db": 15,
    "codes_upstream": 86737,
    "codes_db": 257509,
    "codes_missing_in_db": 12,
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
  "csv_sha256": "bca8376bfbe2e2a582caa8b8aa74f451279ea2f9c605023deda19788950973ca",
  "csv_size_bytes": 26851022,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261001_025721Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211286,
  "items_db": 213107,
  "items_missing_in_db": 15,
  "codes_upstream": 86737,
  "codes_db": 257509,
  "codes_missing_in_db": 12,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 15,
  "db_inserted_codes": 11
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 257535,
  "distinct_bl_part_id": 177911,
  "null_boid": 179356,
  "null_weight": 102215,
  "null_bk_part_id": 26,
  "null_bk_part_key": 26,
  "null_api_item_type": 26,
  "null_brikick_name": 26,
  "null_part_name": 103814,
  "null_element_id": 174298,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179356`
- null_weight: `102215`
- corruption_pattern_count: `0`
