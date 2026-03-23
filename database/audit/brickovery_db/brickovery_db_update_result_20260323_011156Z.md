# Brikick DB Post-Update Report

- created_at_utc: `20260323_011156Z`
- db_path: `database/brickovery.db`
- db_sha256: `af0c84aa1756a5b0c158286a8abbb024c4d42a6a9d1950165e0c7cd6dee1642b`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260323_011145Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260323_011145Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "91119db3dfec7850faf0fb1c1cfc579b6fcb56617c23d8ce92c8d0f1526b834d",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260323_011145Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203775,
    "items_db": 203809,
    "items_missing_in_db": 58,
    "codes_upstream": 84052,
    "codes_db": 244233,
    "codes_missing_in_db": 2,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "2c0ed6e7b02bfd27963ad3ebfdc878f6432c468103428acf45301af40caf5c77",
  "csv_size_bytes": 26091360,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260323_011145Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203775,
  "items_db": 203809,
  "items_missing_in_db": 58,
  "codes_upstream": 84052,
  "codes_db": 244233,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 58,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 244293,
  "distinct_bl_part_id": 169571,
  "null_boid": 166125,
  "null_weight": 90455,
  "null_bk_part_id": 60,
  "null_bk_part_key": 60,
  "null_api_item_type": 60,
  "null_brikick_name": 60,
  "null_part_name": 90572,
  "null_element_id": 161056,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `166125`
- null_weight: `90455`
- corruption_pattern_count: `0`
