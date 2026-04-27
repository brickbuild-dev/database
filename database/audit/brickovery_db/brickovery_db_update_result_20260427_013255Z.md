# Brikick DB Post-Update Report

- created_at_utc: `20260427_013255Z`
- db_path: `database/brickovery.db`
- db_sha256: `db24218baed193484f518b419724e8d6bb0f832e4c607824ddd9371946c886e1`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260427_013244Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260427_013244Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "bd6445d9914f5fbc4dcef8c30622f7b83e63f7370453b411283fe38ba41e8704",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260427_013244Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205352,
    "items_db": 205662,
    "items_missing_in_db": 64,
    "codes_upstream": 84259,
    "codes_db": 246297,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "63d6702b49afc1c0f8c810e1b5c2668f794caced1a287872e2da5e66ad044aba",
  "csv_size_bytes": 26207131,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260427_013244Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205352,
  "items_db": 205662,
  "items_missing_in_db": 64,
  "codes_upstream": 84259,
  "codes_db": 246297,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 64,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246361,
  "distinct_bl_part_id": 171338,
  "null_boid": 168187,
  "null_weight": 92406,
  "null_bk_part_id": 64,
  "null_bk_part_key": 64,
  "null_api_item_type": 64,
  "null_brikick_name": 64,
  "null_part_name": 92640,
  "null_element_id": 163124,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168187`
- null_weight: `92406`
- corruption_pattern_count: `0`
