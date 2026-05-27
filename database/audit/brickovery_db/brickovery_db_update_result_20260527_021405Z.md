# Brikick DB Post-Update Report

- created_at_utc: `20260527_021405Z`
- db_path: `database/brickovery.db`
- db_sha256: `1f2995572e9d7602fe85741ef7f7a2387796ac2006c4cf5d6af05b501886c4ae`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260527_021353Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260527_021353Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "1b1c7954c1a2ed3f240cf754bddd39ef3d09aef514c932e9526a992249a1f1fe",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260527_021353Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205942,
    "items_db": 206500,
    "items_missing_in_db": 12,
    "codes_upstream": 84410,
    "codes_db": 248173,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "a15a2fdfebc07ac2884de1c1aad053a90712821424f59b3593c4d7f754226d1a",
  "csv_size_bytes": 26315555,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260527_021353Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205942,
  "items_db": 206500,
  "items_missing_in_db": 12,
  "codes_upstream": 84410,
  "codes_db": 248173,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 12,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248186,
  "distinct_bl_part_id": 172033,
  "null_boid": 170011,
  "null_weight": 93623,
  "null_bk_part_id": 13,
  "null_bk_part_key": 13,
  "null_api_item_type": 13,
  "null_brikick_name": 13,
  "null_part_name": 94465,
  "null_element_id": 164949,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `170011`
- null_weight: `93623`
- corruption_pattern_count: `0`
