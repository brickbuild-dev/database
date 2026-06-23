# Brikick DB Post-Update Report

- created_at_utc: `20260623_020721Z`
- db_path: `database/brickovery.db`
- db_sha256: `1f5645c29c3d6f41c7b487265463e49d98d763920cdb8f0b2cdadf2138dac313`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260623_020709Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260623_020709Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "73add17bcea267cbf366cc58cdd672dd454a36c209d71b15f3ccd9de5a1cbb41",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260623_020709Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207364,
    "items_db": 207983,
    "items_missing_in_db": 15,
    "codes_upstream": 84944,
    "codes_db": 250142,
    "codes_missing_in_db": 7,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "aa4f7b462d76b806f462b2b01c43c7f3b8d241379fadfdea6c2a58ad503ab84c",
  "csv_size_bytes": 26428798,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260623_020709Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207364,
  "items_db": 207983,
  "items_missing_in_db": 15,
  "codes_upstream": 84944,
  "codes_db": 250142,
  "codes_missing_in_db": 7,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 15,
  "db_inserted_codes": 6
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250163,
  "distinct_bl_part_id": 173251,
  "null_boid": 171987,
  "null_weight": 95497,
  "null_bk_part_id": 21,
  "null_bk_part_key": 21,
  "null_api_item_type": 21,
  "null_brikick_name": 21,
  "null_part_name": 96442,
  "null_element_id": 166926,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171987`
- null_weight: `95497`
- corruption_pattern_count: `0`
