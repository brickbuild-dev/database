# Brikick DB Post-Update Report

- created_at_utc: `20260604_023824Z`
- db_path: `database/brickovery.db`
- db_sha256: `668b496549571d172410766902ae948bc4c49c09b4f93c9f6308839462ad83be`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260604_023813Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260604_023813Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "308648052e44c4cd90298b6e4548555b3d1498de4a4342fdde2967916bc248f2",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260604_023813Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 206529,
    "items_db": 207093,
    "items_missing_in_db": 27,
    "codes_upstream": 84454,
    "codes_db": 248791,
    "codes_missing_in_db": 16,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "09421e88bb72b5cd7957d087171b9c65ae7a42ef8cbedb3ca3af4ebc82ddeef7",
  "csv_size_bytes": 26351738,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260604_023813Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 206529,
  "items_db": 207093,
  "items_missing_in_db": 27,
  "codes_upstream": 84454,
  "codes_db": 248791,
  "codes_missing_in_db": 16,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 27,
  "db_inserted_codes": 14
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248832,
  "distinct_bl_part_id": 172383,
  "null_boid": 170657,
  "null_weight": 94268,
  "null_bk_part_id": 41,
  "null_bk_part_key": 41,
  "null_api_item_type": 41,
  "null_brikick_name": 41,
  "null_part_name": 95111,
  "null_element_id": 165595,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `170657`
- null_weight: `94268`
- corruption_pattern_count: `0`
