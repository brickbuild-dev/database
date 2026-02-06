# Brikick DB Post-Update Report

- created_at_utc: `20260205_232516Z`
- db_path: `database/brickovery.db`
- db_sha256: `ddc199af64bd1e7e77820f564e86b629bb05b4623b3fb7f79f5ec701c6ff3b56`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260205_232504Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260205_232504Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "4f076871ebaadb2236ce426fc291ea49486743958028380e0e5a17e35d9128e1",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260205_232504Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202403,
    "items_db": 202401,
    "items_missing_in_db": 2,
    "codes_upstream": 83280,
    "codes_db": 242094,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "ba13922c337505517a8d5239c5c5bf73d5db96655a959dcd92915e75ef1f7b15",
  "csv_size_bytes": 25487743,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260205_232504Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202403,
  "items_db": 202401,
  "items_missing_in_db": 2,
  "codes_upstream": 83280,
  "codes_db": 242094,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 2,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242096,
  "distinct_bl_part_id": 168259,
  "null_boid": 242096,
  "null_weight": 92165,
  "null_bk_part_id": 2,
  "null_bk_part_key": 2,
  "null_api_item_type": 2,
  "null_brikick_name": 2,
  "null_part_name": 88375,
  "null_element_id": 158859,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `242096`
- null_weight: `92165`
- corruption_pattern_count: `0`
