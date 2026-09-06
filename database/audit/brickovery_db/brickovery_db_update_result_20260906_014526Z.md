# Brikick DB Post-Update Report

- created_at_utc: `20260906_014526Z`
- db_path: `database/brickovery.db`
- db_sha256: `b3f5788eafb6d3e7398f76a70e7e9cb0d3310e2b6fc6e5eda52b2ff6e5ae0903`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260906_014515Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260906_014515Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "594e05a0d2a0ad33164d59a908fe2fa3b574cd37cd22a2dcf5fdc97e18d6dfd1",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260906_014515Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210311,
    "items_db": 211123,
    "items_missing_in_db": 24,
    "codes_upstream": 86432,
    "codes_db": 254829,
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
  "csv_sha256": "9978ef80151b40cc81084e34df828f1df435c4ef50b87a355ad16d725aefce82",
  "csv_size_bytes": 26697598,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260906_014515Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210311,
  "items_db": 211123,
  "items_missing_in_db": 24,
  "codes_upstream": 86432,
  "codes_db": 254829,
  "codes_missing_in_db": 15,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 24,
  "db_inserted_codes": 15
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254868,
  "distinct_bl_part_id": 176021,
  "null_boid": 176691,
  "null_weight": 99634,
  "null_bk_part_id": 39,
  "null_bk_part_key": 39,
  "null_api_item_type": 39,
  "null_brikick_name": 39,
  "null_part_name": 101147,
  "null_element_id": 171631,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176691`
- null_weight: `99634`
- corruption_pattern_count: `0`
