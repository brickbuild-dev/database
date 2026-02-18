# Brikick DB Post-Update Report

- created_at_utc: `20260218_051655Z`
- db_path: `database/brickovery.db`
- db_sha256: `30248ab3bf25667b8bb73149b9aa1b4ffd2c8b3339bfdde9dc380d872ee1970d`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260218_051644Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260218_051644Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "7ff69e3fad81210d2fd4449995c7bd2c99aedb89d10c35cb5250ff9422520b52",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260218_051644Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202524,
    "items_db": 202529,
    "items_missing_in_db": 2,
    "codes_upstream": 83441,
    "codes_db": 242364,
    "codes_missing_in_db": 11,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "ef0a168aa91d658b95dd0650a243aba6f5d2b6d5eb8b3e925d106ab41fb0a5e2",
  "csv_size_bytes": 25984060,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260218_051644Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202524,
  "items_db": 202529,
  "items_missing_in_db": 2,
  "codes_upstream": 83441,
  "codes_db": 242364,
  "codes_missing_in_db": 11,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 2,
  "db_inserted_codes": 11
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242377,
  "distinct_bl_part_id": 168373,
  "null_boid": 164210,
  "null_weight": 88792,
  "null_bk_part_id": 13,
  "null_bk_part_key": 13,
  "null_api_item_type": 13,
  "null_brikick_name": 13,
  "null_part_name": 88656,
  "null_element_id": 159140,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `164210`
- null_weight: `88792`
- corruption_pattern_count: `0`
