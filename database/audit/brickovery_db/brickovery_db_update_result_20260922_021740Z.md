# Brikick DB Post-Update Report

- created_at_utc: `20260922_021740Z`
- db_path: `database/brickovery.db`
- db_sha256: `6a49fd9815f48f59cf2a63e5576592e9142801b2dc88072e309c4d12270bfb59`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260922_021728Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260922_021728Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "b1c42593e17bf303db20ef8d2bb02f815e63781fcfb97c453c6e22867b6de928",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260922_021728Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211079,
    "items_db": 211932,
    "items_missing_in_db": 24,
    "codes_upstream": 86709,
    "codes_db": 255947,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [
      "Royal Blue",
      "Speckle Copper",
      "Speckle Gold",
      "Speckle Silver"
    ],
    "unknown_color_tokens_count": 4,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "587b32953fa7bc438e9f43914ef96f855e9d9eddf8f0fd7ceb80a71029fa3f66",
  "csv_size_bytes": 26760962,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260922_021728Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211079,
  "items_db": 211932,
  "items_missing_in_db": 24,
  "codes_upstream": 86709,
  "codes_db": 255947,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 24,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255972,
  "distinct_bl_part_id": 176762,
  "null_boid": 177795,
  "null_weight": 100661,
  "null_bk_part_id": 25,
  "null_bk_part_key": 25,
  "null_api_item_type": 25,
  "null_brikick_name": 25,
  "null_part_name": 102251,
  "null_element_id": 172735,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177795`
- null_weight: `100661`
- corruption_pattern_count: `0`
