# Brikick DB Post-Update Report

- created_at_utc: `20260321_010243Z`
- db_path: `database/brickovery.db`
- db_sha256: `be87a21fc691fd4dae713ede20a89b82bc1b0b2f46301a914038036adeb3d4e9`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260321_010232Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260321_010232Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "87a7474024fb5aebc5d5aed158a73ba5a66c62f092c13c7335dce6c62b6a5b5e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260321_010232Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203717,
    "items_db": 203775,
    "items_missing_in_db": 23,
    "codes_upstream": 84044,
    "codes_db": 244182,
    "codes_missing_in_db": 8,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "b16b3c927ffb71087371789c123c011e58d7811e252debe1d1a76577b5bb889f",
  "csv_size_bytes": 26088555,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260321_010232Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203717,
  "items_db": 203775,
  "items_missing_in_db": 23,
  "codes_upstream": 84044,
  "codes_db": 244182,
  "codes_missing_in_db": 8,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 23,
  "db_inserted_codes": 8
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 244213,
  "distinct_bl_part_id": 169502,
  "null_boid": 166046,
  "null_weight": 90387,
  "null_bk_part_id": 31,
  "null_bk_part_key": 31,
  "null_api_item_type": 31,
  "null_brikick_name": 31,
  "null_part_name": 90492,
  "null_element_id": 160976,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `166046`
- null_weight: `90387`
- corruption_pattern_count: `0`
