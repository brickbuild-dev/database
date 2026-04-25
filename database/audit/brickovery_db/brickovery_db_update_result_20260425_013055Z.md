# Brikick DB Post-Update Report

- created_at_utc: `20260425_013055Z`
- db_path: `database/brickovery.db`
- db_sha256: `2a829a7e35bd0fe00d76d5cd8551ce5117ee51ecc62ac78cf443289061949c37`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260425_013044Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260425_013044Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "9994d2c218fd8ac4c2547a83ddd0b0267838646b935db3562db6ac8aa9359c08",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260425_013044Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205285,
    "items_db": 205653,
    "items_missing_in_db": 1,
    "codes_upstream": 84257,
    "codes_db": 246277,
    "codes_missing_in_db": 10,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "c12c66773f7da1f1559c4d268d73673d43851b2125d189c03634b4eb79370ee0",
  "csv_size_bytes": 26206003,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260425_013044Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205285,
  "items_db": 205653,
  "items_missing_in_db": 1,
  "codes_upstream": 84257,
  "codes_db": 246277,
  "codes_missing_in_db": 10,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 1,
  "db_inserted_codes": 10
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246288,
  "distinct_bl_part_id": 171287,
  "null_boid": 168114,
  "null_weight": 92343,
  "null_bk_part_id": 11,
  "null_bk_part_key": 11,
  "null_api_item_type": 11,
  "null_brikick_name": 11,
  "null_part_name": 92567,
  "null_element_id": 163051,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168114`
- null_weight: `92343`
- corruption_pattern_count: `0`
