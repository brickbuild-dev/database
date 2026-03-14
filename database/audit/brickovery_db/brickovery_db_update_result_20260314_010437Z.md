# Brikick DB Post-Update Report

- created_at_utc: `20260314_010437Z`
- db_path: `database/brickovery.db`
- db_sha256: `4d82f45ea23594f833de19c051b840a8bd7928ee71eefc92c0dd4c9b30cfd509`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260314_010426Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260314_010426Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "00e2a38d09e53c283b7015386a1e710386211f0188900c7ebb721cec628d8549",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260314_010426Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203517,
    "items_db": 203553,
    "items_missing_in_db": 34,
    "codes_upstream": 83951,
    "codes_db": 243875,
    "codes_missing_in_db": 9,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "30c046a1d95cb9bb7ff8293211d7582f7080215603ced198718cf4112802ba97",
  "csv_size_bytes": 26070825,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260314_010426Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203517,
  "items_db": 203553,
  "items_missing_in_db": 34,
  "codes_upstream": 83951,
  "codes_db": 243875,
  "codes_missing_in_db": 9,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 34,
  "db_inserted_codes": 9
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243918,
  "distinct_bl_part_id": 169298,
  "null_boid": 165751,
  "null_weight": 90098,
  "null_bk_part_id": 43,
  "null_bk_part_key": 43,
  "null_api_item_type": 43,
  "null_brikick_name": 43,
  "null_part_name": 90197,
  "null_element_id": 160681,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165751`
- null_weight: `90098`
- corruption_pattern_count: `0`
