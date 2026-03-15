# Brikick DB Post-Update Report

- created_at_utc: `20260315_011524Z`
- db_path: `database/brickovery.db`
- db_sha256: `3edc9e2e2d4e1075793d8c0e71b487cb867063daf181a139182a428146eb4bf5`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260315_011513Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260315_011513Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "622d9aeb46b3775d6884d672cd0d596631bb79e63e9f6ec80c6132f265d92c80",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260315_011513Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203563,
    "items_db": 203587,
    "items_missing_in_db": 46,
    "codes_upstream": 83961,
    "codes_db": 243918,
    "codes_missing_in_db": 11,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "a971eb883dd76ec4aefe16b8bf8f9952f50721bb3f679ec2ee12d966c5a76067",
  "csv_size_bytes": 26073287,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260315_011513Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203563,
  "items_db": 203587,
  "items_missing_in_db": 46,
  "codes_upstream": 83961,
  "codes_db": 243918,
  "codes_missing_in_db": 11,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 46,
  "db_inserted_codes": 10
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243974,
  "distinct_bl_part_id": 169343,
  "null_boid": 165807,
  "null_weight": 90151,
  "null_bk_part_id": 56,
  "null_bk_part_key": 56,
  "null_api_item_type": 56,
  "null_brikick_name": 56,
  "null_part_name": 90253,
  "null_element_id": 160737,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165807`
- null_weight: `90151`
- corruption_pattern_count: `0`
