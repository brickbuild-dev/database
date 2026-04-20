# Brikick DB Post-Update Report

- created_at_utc: `20260420_012953Z`
- db_path: `database/brickovery.db`
- db_sha256: `1c90a5dac2dc0129df67bb2b7db250118836c3aacb5a3c1b321953a264431e9f`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260420_012943Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260420_012943Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "ff3df0d46451da2d644ee57e47d58ddc8637e6123feaa770ca54d723a2835087",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260420_012943Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205256,
    "items_db": 205593,
    "items_missing_in_db": 22,
    "codes_upstream": 84170,
    "codes_db": 246118,
    "codes_missing_in_db": 8,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "289e13da2f72ea50aad41f8351e26b7677597d9070615bf5188f1e480b99ce48",
  "csv_size_bytes": 26196913,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260420_012943Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205256,
  "items_db": 205593,
  "items_missing_in_db": 22,
  "codes_upstream": 84170,
  "codes_db": 246118,
  "codes_missing_in_db": 8,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 22,
  "db_inserted_codes": 8
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246148,
  "distinct_bl_part_id": 171253,
  "null_boid": 167978,
  "null_weight": 92279,
  "null_bk_part_id": 30,
  "null_bk_part_key": 30,
  "null_api_item_type": 30,
  "null_brikick_name": 30,
  "null_part_name": 92427,
  "null_element_id": 162911,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167978`
- null_weight: `92279`
- corruption_pattern_count: `0`
