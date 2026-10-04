# Brikick DB Post-Update Report

- created_at_utc: `20261004_031737Z`
- db_path: `database/brickovery.db`
- db_sha256: `03eb6c5e1ab96f8795149b5cfb2c0e7277439014abc0fa43835dbbe64a6164af`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261004_031725Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261004_031725Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "c0f30e456edd5296ce88cde6e30a455a7f7d3466a9cadf229fa6217a7a1f03ad",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261004_031725Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211435,
    "items_db": 213237,
    "items_missing_in_db": 33,
    "codes_upstream": 86786,
    "codes_db": 257660,
    "codes_missing_in_db": 35,
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
  "csv_sha256": "45c290e0a829d26790d8793651b9cde3a54b3b374d530a45bb89444a9640a20e",
  "csv_size_bytes": 26859858,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261004_031725Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211435,
  "items_db": 213237,
  "items_missing_in_db": 33,
  "codes_upstream": 86786,
  "codes_db": 257660,
  "codes_missing_in_db": 35,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 33,
  "db_inserted_codes": 32
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 257725,
  "distinct_bl_part_id": 178021,
  "null_boid": 179546,
  "null_weight": 102396,
  "null_bk_part_id": 65,
  "null_bk_part_key": 65,
  "null_api_item_type": 65,
  "null_brikick_name": 65,
  "null_part_name": 104004,
  "null_element_id": 174488,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179546`
- null_weight: `102396`
- corruption_pattern_count: `0`
