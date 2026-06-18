# Brikick DB Post-Update Report

- created_at_utc: `20260618_023719Z`
- db_path: `database/brickovery.db`
- db_sha256: `16fcea75271107d02091738a1ad5a2722965c460e635de8a8cec58b2c4881097`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260618_023708Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260618_023708Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "3b70607450ad809f52da412d063c9eac4b44d2f1259a83fc28ba000be36973a5",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260618_023708Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207264,
    "items_db": 207866,
    "items_missing_in_db": 17,
    "codes_upstream": 84898,
    "codes_db": 249961,
    "codes_missing_in_db": 24,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "1953c1889eda860b86f29698b7940445a95afe57376ed83db7025fbfabc23ec8",
  "csv_size_bytes": 26418204,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260618_023708Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207264,
  "items_db": 207866,
  "items_missing_in_db": 17,
  "codes_upstream": 84898,
  "codes_db": 249961,
  "codes_missing_in_db": 24,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 17,
  "db_inserted_codes": 24
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250002,
  "distinct_bl_part_id": 173140,
  "null_boid": 171826,
  "null_weight": 95340,
  "null_bk_part_id": 41,
  "null_bk_part_key": 41,
  "null_api_item_type": 41,
  "null_brikick_name": 41,
  "null_part_name": 96281,
  "null_element_id": 166765,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171826`
- null_weight: `95340`
- corruption_pattern_count: `0`
