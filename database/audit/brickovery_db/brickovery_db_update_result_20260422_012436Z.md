# Brikick DB Post-Update Report

- created_at_utc: `20260422_012436Z`
- db_path: `database/brickovery.db`
- db_sha256: `1440c5ee08632b44749fff2759881aee75c416f4edf461c288977eeff13a6e6a`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260422_012424Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260422_012424Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "a132197db368fcd6d8110b65f01506b98822f4174a153a84776d3ad46d0bfdc9",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260422_012424Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205278,
    "items_db": 205620,
    "items_missing_in_db": 24,
    "codes_upstream": 84171,
    "codes_db": 246168,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "c8977e05733d56b242a42a472df56eaf43e1da83bf0b8333563b5cfe0e250897",
  "csv_size_bytes": 26199806,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260422_012424Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205278,
  "items_db": 205620,
  "items_missing_in_db": 24,
  "codes_upstream": 84171,
  "codes_db": 246168,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 24,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246192,
  "distinct_bl_part_id": 171278,
  "null_boid": 168018,
  "null_weight": 92322,
  "null_bk_part_id": 24,
  "null_bk_part_key": 24,
  "null_api_item_type": 24,
  "null_brikick_name": 24,
  "null_part_name": 92471,
  "null_element_id": 162955,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168018`
- null_weight: `92322`
- corruption_pattern_count: `0`
