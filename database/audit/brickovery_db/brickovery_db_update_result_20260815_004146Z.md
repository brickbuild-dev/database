# Brikick DB Post-Update Report

- created_at_utc: `20260815_004146Z`
- db_path: `database/brickovery.db`
- db_sha256: `6790be3a6e38e71aea5a7db1a2e7c9d8969a11b8998a67f9c082b8c1c3a1c9db`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260815_004135Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260815_004135Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "4990efb0af5892cd3eb9e58a32c68108f3ef68b791bd27241e3cd25c4c905a61",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260815_004135Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209594,
    "items_db": 210337,
    "items_missing_in_db": 38,
    "codes_upstream": 86174,
    "codes_db": 253734,
    "codes_missing_in_db": 30,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "28dd742b137404fc184e7783d8c679b062f0174cdc89ed068810abc840c39bb7",
  "csv_size_bytes": 26633396,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260815_004135Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209594,
  "items_db": 210337,
  "items_missing_in_db": 38,
  "codes_upstream": 86174,
  "codes_db": 253734,
  "codes_missing_in_db": 30,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 38,
  "db_inserted_codes": 27
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253799,
  "distinct_bl_part_id": 175423,
  "null_boid": 175622,
  "null_weight": 98603,
  "null_bk_part_id": 65,
  "null_bk_part_key": 65,
  "null_api_item_type": 65,
  "null_brikick_name": 65,
  "null_part_name": 100078,
  "null_element_id": 170562,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175622`
- null_weight: `98603`
- corruption_pattern_count: `0`
