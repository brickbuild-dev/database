# Brikick DB Post-Update Report

- created_at_utc: `20260313_011246Z`
- db_path: `database/brickovery.db`
- db_sha256: `849c176a8a1a31502b147480c53e7529f4c26bec28ec34bb87c6af70c0b6b035`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260313_011235Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260313_011235Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "76d67b6f556a436fb4e12e5647bd33548c705f6c8fa354849552b83cae0f96ee",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260313_011235Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203485,
    "items_db": 203534,
    "items_missing_in_db": 19,
    "codes_upstream": 83941,
    "codes_db": 243853,
    "codes_missing_in_db": 3,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "d967676fbd3c05845ea637877b2707212fa86b20754d95d02e1939c87e5eaff6",
  "csv_size_bytes": 26069591,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260313_011235Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203485,
  "items_db": 203534,
  "items_missing_in_db": 19,
  "codes_upstream": 83941,
  "codes_db": 243853,
  "codes_missing_in_db": 3,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 19,
  "db_inserted_codes": 3
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243875,
  "distinct_bl_part_id": 169264,
  "null_boid": 165708,
  "null_weight": 90055,
  "null_bk_part_id": 22,
  "null_bk_part_key": 22,
  "null_api_item_type": 22,
  "null_brikick_name": 22,
  "null_part_name": 90154,
  "null_element_id": 160638,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165708`
- null_weight: `90055`
- corruption_pattern_count: `0`
