# Brikick DB Post-Update Report

- created_at_utc: `20260301_011248Z`
- db_path: `database/brickovery.db`
- db_sha256: `4cb51c437d1b6a3a48c9c81f9fe0a878b3448a816d6abf97915e8529bfabd640`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260301_011237Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260301_011237Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "346eee88d78b0cdacd76e8f500b5a156bac88569aa4a31e4f6f7f0ca83f7acc7",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260301_011237Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202999,
    "items_db": 202599,
    "items_missing_in_db": 446,
    "codes_upstream": 83654,
    "codes_db": 242539,
    "codes_missing_in_db": 120,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "acbd39b54dbbe89def47a23a7afe389e97483e821cb53301eafb6b673c8307ba",
  "csv_size_bytes": 25994008,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260301_011237Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202999,
  "items_db": 202599,
  "items_missing_in_db": 446,
  "codes_upstream": 83654,
  "codes_db": 242539,
  "codes_missing_in_db": 120,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 446,
  "db_inserted_codes": 120
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243105,
  "distinct_bl_part_id": 168849,
  "null_boid": 164938,
  "null_weight": 89416,
  "null_bk_part_id": 566,
  "null_bk_part_key": 566,
  "null_api_item_type": 566,
  "null_brikick_name": 566,
  "null_part_name": 89384,
  "null_element_id": 159868,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `164938`
- null_weight: `89416`
- corruption_pattern_count: `0`
