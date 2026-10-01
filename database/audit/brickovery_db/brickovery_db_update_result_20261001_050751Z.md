# Brikick DB Post-Update Report

- created_at_utc: `20261001_050751Z`
- db_path: `database/brickovery.db`
- db_sha256: `896bbefb8598a42c708ebc73914be203e8facfb74c9c6a3e954a4937cabced3b`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261001_050740Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261001_050740Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "46af8a5cf5359be331f01f28cec5766437f34d2bf5c1b9a0394b2097d10b33a5",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261001_050740Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211299,
    "items_db": 213122,
    "items_missing_in_db": 13,
    "codes_upstream": 86738,
    "codes_db": 257535,
    "codes_missing_in_db": 1,
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
  "csv_sha256": "f37f1a8ee79b25bc4d8c7c7bab37abed6f5405f1cd1c9c6c58e777eebd4ee959",
  "csv_size_bytes": 26852552,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261001_050740Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211299,
  "items_db": 213122,
  "items_missing_in_db": 13,
  "codes_upstream": 86738,
  "codes_db": 257535,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 13,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 257548,
  "distinct_bl_part_id": 177916,
  "null_boid": 179369,
  "null_weight": 102224,
  "null_bk_part_id": 13,
  "null_bk_part_key": 13,
  "null_api_item_type": 13,
  "null_brikick_name": 13,
  "null_part_name": 103827,
  "null_element_id": 174311,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179369`
- null_weight: `102224`
- corruption_pattern_count: `0`
