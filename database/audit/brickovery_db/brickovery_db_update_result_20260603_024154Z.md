# Brikick DB Post-Update Report

- created_at_utc: `20260603_024154Z`
- db_path: `database/brickovery.db`
- db_sha256: `f3681a17f0343ba4e53efb251cd966920bdabc6f2be6430dc9880233df541f50`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260603_024143Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260603_024143Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "30cc0d83dd5e8fb4d91779247d2ff08d98f14d502ad391149fcfe5b51768dced",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260603_024143Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 206502,
    "items_db": 207049,
    "items_missing_in_db": 44,
    "codes_upstream": 84437,
    "codes_db": 248739,
    "codes_missing_in_db": 11,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "f1eaf139543d5406758d602ffc6ce7621a4b37cfd69392374ea5fc2584cc1ee4",
  "csv_size_bytes": 26348840,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260603_024143Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 206502,
  "items_db": 207049,
  "items_missing_in_db": 44,
  "codes_upstream": 84437,
  "codes_db": 248739,
  "codes_missing_in_db": 11,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 44,
  "db_inserted_codes": 8
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248791,
  "distinct_bl_part_id": 172360,
  "null_boid": 170616,
  "null_weight": 94227,
  "null_bk_part_id": 52,
  "null_bk_part_key": 52,
  "null_api_item_type": 52,
  "null_brikick_name": 52,
  "null_part_name": 95070,
  "null_element_id": 165554,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `170616`
- null_weight: `94227`
- corruption_pattern_count: `0`
