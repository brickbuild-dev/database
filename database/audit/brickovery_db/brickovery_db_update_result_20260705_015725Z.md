# Brikick DB Post-Update Report

- created_at_utc: `20260705_015725Z`
- db_path: `database/brickovery.db`
- db_sha256: `de1fa50acb77e02d095376ce5cd86471e532ff8befd984747a8a3862c3b2ce44`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260705_015712Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260705_015712Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "65abae1193cb14d61565261c7acc9fa5e075457f89e7b9eef4e1a698ce0d77e1",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260705_015712Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207722,
    "items_db": 208380,
    "items_missing_in_db": 20,
    "codes_upstream": 85204,
    "codes_db": 250813,
    "codes_missing_in_db": 10,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "8f2100dcc027bca98844ac2b5ee928960cd61096329536dd78a5684fd9f0f7d8",
  "csv_size_bytes": 26467852,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260705_015712Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207722,
  "items_db": 208380,
  "items_missing_in_db": 20,
  "codes_upstream": 85204,
  "codes_db": 250813,
  "codes_missing_in_db": 10,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 20,
  "db_inserted_codes": 10
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250843,
  "distinct_bl_part_id": 173623,
  "null_boid": 172667,
  "null_weight": 96117,
  "null_bk_part_id": 30,
  "null_bk_part_key": 30,
  "null_api_item_type": 30,
  "null_brikick_name": 30,
  "null_part_name": 97122,
  "null_element_id": 167606,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172667`
- null_weight: `96117`
- corruption_pattern_count: `0`
