# Brikick DB Post-Update Report

- created_at_utc: `20261005_025231Z`
- db_path: `database/brickovery.db`
- db_sha256: `032579460d44dd38003b0d346979dea54157d6872f7713368df0f720656af8ee`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261005_025219Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261005_025219Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "6a147a9708878fdbe5cfe4b64e92871efa7d330a457b7b3e1e014be197464b3f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261005_025219Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211453,
    "items_db": 213270,
    "items_missing_in_db": 24,
    "codes_upstream": 86823,
    "codes_db": 257725,
    "codes_missing_in_db": 37,
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
  "csv_sha256": "bab8ba41c8c5f6e8a7e12ef953dc9ae98d52472d1fc8e5e68916f84878c9adba",
  "csv_size_bytes": 26863663,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261005_025219Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211453,
  "items_db": 213270,
  "items_missing_in_db": 24,
  "codes_upstream": 86823,
  "codes_db": 257725,
  "codes_missing_in_db": 37,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 24,
  "db_inserted_codes": 37
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 257786,
  "distinct_bl_part_id": 178037,
  "null_boid": 179607,
  "null_weight": 102448,
  "null_bk_part_id": 61,
  "null_bk_part_key": 61,
  "null_api_item_type": 61,
  "null_brikick_name": 61,
  "null_part_name": 104065,
  "null_element_id": 174549,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179607`
- null_weight: `102448`
- corruption_pattern_count: `0`
