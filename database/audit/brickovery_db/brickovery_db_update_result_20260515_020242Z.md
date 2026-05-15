# Brikick DB Post-Update Report

- created_at_utc: `20260515_020242Z`
- db_path: `database/brickovery.db`
- db_sha256: `c590f25365f393e8384f2d539abf84a73a0156dce4204c5e56e9023e0dbc0286`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260515_020230Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260515_020230Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "fff90a28e873a859c060f59656288ffb7201fd8895c436bc5337ba63832c928e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260515_020230Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205845,
    "items_db": 206187,
    "items_missing_in_db": 128,
    "codes_upstream": 84366,
    "codes_db": 247636,
    "codes_missing_in_db": 133,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "079e0ef546264827293f805c8f2b260fd15cb870dd1c7b3c90dbde81f4ffa462",
  "csv_size_bytes": 26284762,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260515_020230Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205845,
  "items_db": 206187,
  "items_missing_in_db": 128,
  "codes_upstream": 84366,
  "codes_db": 247636,
  "codes_missing_in_db": 133,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 128,
  "db_inserted_codes": 126
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247890,
  "distinct_bl_part_id": 171849,
  "null_boid": 169715,
  "null_weight": 93372,
  "null_bk_part_id": 254,
  "null_bk_part_key": 254,
  "null_api_item_type": 254,
  "null_brikick_name": 254,
  "null_part_name": 94169,
  "null_element_id": 164653,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169715`
- null_weight: `93372`
- corruption_pattern_count: `0`
