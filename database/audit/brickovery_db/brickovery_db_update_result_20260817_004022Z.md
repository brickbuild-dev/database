# Brikick DB Post-Update Report

- created_at_utc: `20260817_004022Z`
- db_path: `database/brickovery.db`
- db_sha256: `3891feaa82bcac8876ddbad1c89d0fc802e0cd1aa6647fbfab2b69273ad743ae`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260817_004010Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260817_004010Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "ebb78054db60b3869e4ad183353ec0aefb8ecc85074098f998f7efa5eb5cba3e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260817_004010Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209667,
    "items_db": 210422,
    "items_missing_in_db": 31,
    "codes_upstream": 86234,
    "codes_db": 253873,
    "codes_missing_in_db": 31,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "42fd53355bc9589e14ded1d7a9c64967acf1604adf3470dbf62874d31f893b7c",
  "csv_size_bytes": 26641484,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260817_004010Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209667,
  "items_db": 210422,
  "items_missing_in_db": 31,
  "codes_upstream": 86234,
  "codes_db": 253873,
  "codes_missing_in_db": 31,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 31,
  "db_inserted_codes": 31
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253935,
  "distinct_bl_part_id": 175498,
  "null_boid": 175758,
  "null_weight": 98739,
  "null_bk_part_id": 62,
  "null_bk_part_key": 62,
  "null_api_item_type": 62,
  "null_brikick_name": 62,
  "null_part_name": 100214,
  "null_element_id": 170698,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175758`
- null_weight: `98739`
- corruption_pattern_count: `0`
