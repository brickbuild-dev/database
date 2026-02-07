# Brikick DB Post-Update Report

- created_at_utc: `20260207_003721Z`
- db_path: `database/brickovery.db`
- db_sha256: `bf817f187a1c1ab9e70eeb2f58042bece0577a320413b425c92a7bf0dce4b450`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260207_003709Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260207_003709Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "83ca0090b63772750af167f9d2acd98fc5bd902a735d16a9c2991e1dc1458af9",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260207_003709Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202411,
    "items_db": 202403,
    "items_missing_in_db": 8,
    "codes_upstream": 83290,
    "codes_db": 242096,
    "codes_missing_in_db": 7,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "c896aa56c64d58dd825076e31169c1aa24c5ea60bcc5df93234b9848f24e48de",
  "csv_size_bytes": 25502187,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260207_003709Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202411,
  "items_db": 202403,
  "items_missing_in_db": 8,
  "codes_upstream": 83290,
  "codes_db": 242096,
  "codes_missing_in_db": 7,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 8,
  "db_inserted_codes": 7
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242111,
  "distinct_bl_part_id": 168266,
  "null_boid": 242111,
  "null_weight": 88644,
  "null_bk_part_id": 15,
  "null_bk_part_key": 15,
  "null_api_item_type": 15,
  "null_brikick_name": 15,
  "null_part_name": 88390,
  "null_element_id": 158874,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `242111`
- null_weight: `88644`
- corruption_pattern_count: `0`
