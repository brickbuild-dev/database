# Brikick DB Post-Update Report

- created_at_utc: `20260810_005613Z`
- db_path: `database/brickovery.db`
- db_sha256: `d5a8a2816ac65a5c5e3af0f16aae0b3eddba2e4a2346f1a769fc9a4a7d6b0172`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260810_005601Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260810_005601Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "381d201d269235301e1a158b177ac1ff001add15b347c747e3ede5a944f6d7f1",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260810_005601Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209409,
    "items_db": 210103,
    "items_missing_in_db": 81,
    "codes_upstream": 86019,
    "codes_db": 253375,
    "codes_missing_in_db": 4,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "31d7949e281b946919f1de6891c2665ee2446eeced18923bb8c248494fda6752",
  "csv_size_bytes": 26612658,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260810_005601Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209409,
  "items_db": 210103,
  "items_missing_in_db": 81,
  "codes_upstream": 86019,
  "codes_db": 253375,
  "codes_missing_in_db": 4,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 81,
  "db_inserted_codes": 4
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253460,
  "distinct_bl_part_id": 175235,
  "null_boid": 175283,
  "null_weight": 98268,
  "null_bk_part_id": 85,
  "null_bk_part_key": 85,
  "null_api_item_type": 85,
  "null_brikick_name": 85,
  "null_part_name": 99739,
  "null_element_id": 170223,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175283`
- null_weight: `98268`
- corruption_pattern_count: `0`
