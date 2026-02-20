# Brikick DB Post-Update Report

- created_at_utc: `20260220_050817Z`
- db_path: `database/brickovery.db`
- db_sha256: `81685e0b289f2d7998bc99b8e633be82f6e90774b140930372cce1ccd3632f9a`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260220_050806Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260220_050806Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "0a1b7471a82755f236447a85d6db06e533e5323804a3d1424d75d043272b0dfd",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260220_050806Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202587,
    "items_db": 202557,
    "items_missing_in_db": 37,
    "codes_upstream": 83445,
    "codes_db": 242407,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "6014320e47c990c86aef226af60db61d4b23843fd2b4f97a5eb60a4f62aa020d",
  "csv_size_bytes": 25986487,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260220_050806Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202587,
  "items_db": 202557,
  "items_missing_in_db": 37,
  "codes_upstream": 83445,
  "codes_db": 242407,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 37,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242445,
  "distinct_bl_part_id": 168436,
  "null_boid": 164278,
  "null_weight": 88845,
  "null_bk_part_id": 38,
  "null_bk_part_key": 38,
  "null_api_item_type": 38,
  "null_brikick_name": 38,
  "null_part_name": 88724,
  "null_element_id": 159208,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `164278`
- null_weight: `88845`
- corruption_pattern_count: `0`
