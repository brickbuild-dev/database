# Brikick DB Post-Update Report

- created_at_utc: `20260605_021303Z`
- db_path: `database/brickovery.db`
- db_sha256: `27b89dd866dc8dd26e5f65f24b1856579a05d55feaf818ed5976f9bbf3005761`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260605_021251Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260605_021251Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "d922f01230c7e63db1d0c42f3d7261049412f2b7653c85f1f8850c71a778a407",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260605_021251Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 206557,
    "items_db": 207120,
    "items_missing_in_db": 28,
    "codes_upstream": 84470,
    "codes_db": 248832,
    "codes_missing_in_db": 15,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "80b56b9b3f999a121dd6d493869eb8ead721fa8d0d9f6a66c76580859d270453",
  "csv_size_bytes": 26354140,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260605_021251Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 206557,
  "items_db": 207120,
  "items_missing_in_db": 28,
  "codes_upstream": 84470,
  "codes_db": 248832,
  "codes_missing_in_db": 15,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 28,
  "db_inserted_codes": 14
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248874,
  "distinct_bl_part_id": 172411,
  "null_boid": 170699,
  "null_weight": 94303,
  "null_bk_part_id": 42,
  "null_bk_part_key": 42,
  "null_api_item_type": 42,
  "null_brikick_name": 42,
  "null_part_name": 95153,
  "null_element_id": 165637,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `170699`
- null_weight: `94303`
- corruption_pattern_count: `0`
