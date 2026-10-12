# Brikick DB Post-Update Report

- created_at_utc: `20261012_030527Z`
- db_path: `database/brickovery.db`
- db_sha256: `eb570fa4ea7d18a35856c37b755bbaaa1077c119aabd034f3e80b83bff7dbb3e`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261012_030519Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261012_030519Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "5d75cc209521c4ed4a3d777439bcdef72ec4fce7dbacd9860a238f27a653c94f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261012_030519Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211586,
    "items_db": 213425,
    "items_missing_in_db": 14,
    "codes_upstream": 86968,
    "codes_db": 258050,
    "codes_missing_in_db": 13,
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
  "csv_sha256": "817f00f1223446f0264447ee4b923d97660defaef24ae3d3c91f00b3998d4a22",
  "csv_size_bytes": 26882599,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261012_030519Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211586,
  "items_db": 213425,
  "items_missing_in_db": 14,
  "codes_upstream": 86968,
  "codes_db": 258050,
  "codes_missing_in_db": 13,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 14,
  "db_inserted_codes": 13
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258077,
  "distinct_bl_part_id": 178177,
  "null_boid": 179897,
  "null_weight": 102653,
  "null_bk_part_id": 27,
  "null_bk_part_key": 27,
  "null_api_item_type": 27,
  "null_brikick_name": 27,
  "null_part_name": 104356,
  "null_element_id": 174840,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179897`
- null_weight: `102653`
- corruption_pattern_count: `0`
