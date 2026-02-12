# Brikick DB Post-Update Report

- created_at_utc: `20260212_141844Z`
- db_path: `database/brickovery.db`
- db_sha256: `1cc12aa32f9ca39729a9a9be6eead0912259e69e3a867c8a73d991c5cce837af`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260212_141833Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260212_141833Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "35db7c3cec73a2ba4a9b1c7866c4393c78c2d75f5b5fbe9f64c424db76eb35d2",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260212_141833Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202460,
    "items_db": 202463,
    "items_missing_in_db": 1,
    "codes_upstream": 83313,
    "codes_db": 242185,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "5fe1487b9ea3bd776820b32e4021d805da0b0aae9885533cfb876ae9501d3f46",
  "csv_size_bytes": 25973770,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260212_141833Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202460,
  "items_db": 202463,
  "items_missing_in_db": 1,
  "codes_upstream": 83313,
  "codes_db": 242185,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 1,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242186,
  "distinct_bl_part_id": 168315,
  "null_boid": 164019,
  "null_weight": 88709,
  "null_bk_part_id": 1,
  "null_bk_part_key": 1,
  "null_api_item_type": 1,
  "null_brikick_name": 1,
  "null_part_name": 88465,
  "null_element_id": 158949,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `164019`
- null_weight: `88709`
- corruption_pattern_count: `0`
