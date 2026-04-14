# Brikick DB Post-Update Report

- created_at_utc: `20260414_012621Z`
- db_path: `database/brickovery.db`
- db_sha256: `761cab629b14c288b3f310b3621a74ec08ded61774df83e56c668333cad43c63`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260414_012610Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260414_012610Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "9d74ad79c0c35f96df9d7bc217fa53982b1ca899e738d6595321cfb85a3d8f07",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260414_012610Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205189,
    "items_db": 205531,
    "items_missing_in_db": 6,
    "codes_upstream": 84149,
    "codes_db": 246039,
    "codes_missing_in_db": 5,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "663d51235213dfd2d30cd76286e761ded630aa26c4d5d36ed466301a65902127",
  "csv_size_bytes": 26192379,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260414_012610Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205189,
  "items_db": 205531,
  "items_missing_in_db": 6,
  "codes_upstream": 84149,
  "codes_db": 246039,
  "codes_missing_in_db": 5,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 6,
  "db_inserted_codes": 4
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246049,
  "distinct_bl_part_id": 171183,
  "null_boid": 167879,
  "null_weight": 92187,
  "null_bk_part_id": 10,
  "null_bk_part_key": 10,
  "null_api_item_type": 10,
  "null_brikick_name": 10,
  "null_part_name": 92328,
  "null_element_id": 162812,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167879`
- null_weight: `92187`
- corruption_pattern_count: `0`
