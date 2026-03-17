# Brikick DB Post-Update Report

- created_at_utc: `20260317_010706Z`
- db_path: `database/brickovery.db`
- db_sha256: `fab6c301cb983acacc5f977d7f30bd167409ea8632cb590a5c36126697ed9e40`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260317_010655Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260317_010655Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "710d8c98dcf4cc2cfff1e933198f17aa483c0cdfba2e4e346cc8b9bbbddfab01",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260317_010655Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203630,
    "items_db": 203656,
    "items_missing_in_db": 48,
    "codes_upstream": 83995,
    "codes_db": 244001,
    "codes_missing_in_db": 29,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "89b203f756ad7da2cd882218dcc34c8b325aa3ee025995c28a12df67235e3867",
  "csv_size_bytes": 26078073,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260317_010655Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203630,
  "items_db": 203656,
  "items_missing_in_db": 48,
  "codes_upstream": 83995,
  "codes_db": 244001,
  "codes_missing_in_db": 29,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 48,
  "db_inserted_codes": 28
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 244077,
  "distinct_bl_part_id": 169414,
  "null_boid": 165910,
  "null_weight": 90252,
  "null_bk_part_id": 76,
  "null_bk_part_key": 76,
  "null_api_item_type": 76,
  "null_brikick_name": 76,
  "null_part_name": 90356,
  "null_element_id": 160840,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165910`
- null_weight: `90252`
- corruption_pattern_count: `0`
