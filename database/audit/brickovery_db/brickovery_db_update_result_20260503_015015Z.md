# Brikick DB Post-Update Report

- created_at_utc: `20260503_015015Z`
- db_path: `database/brickovery.db`
- db_sha256: `f238ed19c53c57cf9796d5d503231431dee7c680a2bdf310418dec7f9fbd0562`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260503_015004Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260503_015004Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "7b75d40e4c52641c193a0814da37cfdd2c6495c2004b05ca4e1c1264d215b736",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260503_015004Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205583,
    "items_db": 205906,
    "items_missing_in_db": 73,
    "codes_upstream": 84673,
    "codes_db": 246795,
    "codes_missing_in_db": 170,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "8267397c046e1305b80d5f023ae3b9ac019248a806bfb2c5851135cdcf9a60b3",
  "csv_size_bytes": 26236080,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260503_015004Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205583,
  "items_db": 205906,
  "items_missing_in_db": 73,
  "codes_upstream": 84673,
  "codes_db": 246795,
  "codes_missing_in_db": 170,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 73,
  "db_inserted_codes": 168
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247036,
  "distinct_bl_part_id": 171527,
  "null_boid": 168862,
  "null_weight": 92872,
  "null_bk_part_id": 241,
  "null_bk_part_key": 241,
  "null_api_item_type": 241,
  "null_brikick_name": 241,
  "null_part_name": 93315,
  "null_element_id": 163799,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168862`
- null_weight: `92872`
- corruption_pattern_count: `0`
