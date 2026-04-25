# Brikick DB Post-Update Report

- created_at_utc: `20260425_012224Z`
- db_path: `database/brickovery.db`
- db_sha256: `6cda2f4060c655307b78997d3a1c428dd23b8a4fce7a21afee118edf21095033`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260425_012213Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260425_012213Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "bb95340224c6988e8ceeb55305119b8bcc78cb56b12ccff95a7194ca9191e0f3",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260425_012213Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205285,
    "items_db": 205649,
    "items_missing_in_db": 4,
    "codes_upstream": 84247,
    "codes_db": 246272,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "4ea2f13ebbde888fae1b0431f0f962dba58b8b061d73113f179b8d78985c0868",
  "csv_size_bytes": 26205723,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260425_012213Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205285,
  "items_db": 205649,
  "items_missing_in_db": 4,
  "codes_upstream": 84247,
  "codes_db": 246272,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 4,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246277,
  "distinct_bl_part_id": 171286,
  "null_boid": 168103,
  "null_weight": 92333,
  "null_bk_part_id": 5,
  "null_bk_part_key": 5,
  "null_api_item_type": 5,
  "null_brikick_name": 5,
  "null_part_name": 92556,
  "null_element_id": 163040,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `168103`
- null_weight: `92333`
- corruption_pattern_count: `0`
