# Brikick DB Post-Update Report

- created_at_utc: `20260216_052140Z`
- db_path: `database/brickovery.db`
- db_sha256: `dd772191526946966f909326f215777902a1a22001261bf3cab423ba151e0339`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260216_052129Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260216_052129Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "068bc7b8ac1cc4ca16aa11bea9dacf58aae37012e0d50eb9a1e9896a1ae9031e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260216_052129Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202494,
    "items_db": 202489,
    "items_missing_in_db": 11,
    "codes_upstream": 83337,
    "codes_db": 242230,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "23bc17f459f32b089b000b6eefe1dca271010ced58f1c99777dabd896fe49d02",
  "csv_size_bytes": 25976355,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260216_052129Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202494,
  "items_db": 202489,
  "items_missing_in_db": 11,
  "codes_upstream": 83337,
  "codes_db": 242230,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 11,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242242,
  "distinct_bl_part_id": 168344,
  "null_boid": 164075,
  "null_weight": 88750,
  "null_bk_part_id": 12,
  "null_bk_part_key": 12,
  "null_api_item_type": 12,
  "null_brikick_name": 12,
  "null_part_name": 88521,
  "null_element_id": 159005,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `164075`
- null_weight: `88750`
- corruption_pattern_count: `0`
