# Brikick DB Post-Update Report

- created_at_utc: `20260423_013103Z`
- db_path: `database/brickovery.db`
- db_sha256: `c991f73782d3b5bb5342d84a9dceaa9a72af68306aaf186cf060ea9de7a714df`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260423_013052Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260423_013052Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "8609335c9c62a959cfffdf8b9306edbcdefa18edae2ddc07b1b78827340a8f2f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260423_013052Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205279,
    "items_db": 205644,
    "items_missing_in_db": 2,
    "codes_upstream": 84171,
    "codes_db": 246192,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "f78a6547cf0d0bd03c74f4bbea33cafea5f42b4d6bd722f5f55998928d5a68b7",
  "csv_size_bytes": 26201126,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260423_013052Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205279,
  "items_db": 205644,
  "items_missing_in_db": 2,
  "codes_upstream": 84171,
  "codes_db": 246192,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 2,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246194,
  "distinct_bl_part_id": 171280,
  "null_boid": 168020,
  "null_weight": 92324,
  "null_bk_part_id": 2,
  "null_bk_part_key": 2,
  "null_api_item_type": 2,
  "null_brikick_name": 2,
  "null_part_name": 92473,
  "null_element_id": 162957,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168020`
- null_weight: `92324`
- corruption_pattern_count: `0`
