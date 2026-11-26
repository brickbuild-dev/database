# Brikick DB Post-Update Report

- created_at_utc: `20261126_055248Z`
- db_path: `database/brickovery.db`
- db_sha256: `d3d700280d51587d7f1923631df7cb1f2ba7efc89703854937d4e02660a30fb5`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261126_055239Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261126_055239Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "d41a15a9e24deeaca23c34c805364166cd1bdf421e24f2bcdaef2960ea6f5c7f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261126_055239Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212192,
    "items_db": 214062,
    "items_missing_in_db": 15,
    "codes_upstream": 87198,
    "codes_db": 258920,
    "codes_missing_in_db": 7,
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
  "csv_sha256": "dd1021a4b3265a4a03e641e5e5e078fc7a9d577698ee1f56c38e687f95b30062",
  "csv_size_bytes": 26932623,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261126_055239Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212192,
  "items_db": 214062,
  "items_missing_in_db": 15,
  "codes_upstream": 87198,
  "codes_db": 258920,
  "codes_missing_in_db": 7,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 15,
  "db_inserted_codes": 6
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258941,
  "distinct_bl_part_id": 178770,
  "null_boid": 180761,
  "null_weight": 103467,
  "null_bk_part_id": 21,
  "null_bk_part_key": 21,
  "null_api_item_type": 21,
  "null_brikick_name": 21,
  "null_part_name": 105220,
  "null_element_id": 175704,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180761`
- null_weight: `103467`
- corruption_pattern_count: `0`
