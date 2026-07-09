# Brikick DB Post-Update Report

- created_at_utc: `20260709_015217Z`
- db_path: `database/brickovery.db`
- db_sha256: `2542c8c222ea5c6a647f8a8f4d1ae3151015ffe88da5101d0ae95ca7db151bae`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260709_015205Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260709_015205Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "c3be2bcfa6e2a2c380b4717eba60e1f9b748391a7fe8f93d5afd6ee68d280faf",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260709_015205Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207760,
    "items_db": 208431,
    "items_missing_in_db": 7,
    "codes_upstream": 85243,
    "codes_db": 250893,
    "codes_missing_in_db": 17,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "5d2e2256f1b3d0e0be19f579556ea63fb00b9d7750c499cbd0d337fcb00a9886",
  "csv_size_bytes": 26472528,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260709_015205Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207760,
  "items_db": 208431,
  "items_missing_in_db": 7,
  "codes_upstream": 85243,
  "codes_db": 250893,
  "codes_missing_in_db": 17,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 7,
  "db_inserted_codes": 17
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250917,
  "distinct_bl_part_id": 173658,
  "null_boid": 172741,
  "null_weight": 96187,
  "null_bk_part_id": 24,
  "null_bk_part_key": 24,
  "null_api_item_type": 24,
  "null_brikick_name": 24,
  "null_part_name": 97196,
  "null_element_id": 167680,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172741`
- null_weight: `96187`
- corruption_pattern_count: `0`
