# Brikick DB Post-Update Report

- created_at_utc: `20260613_021324Z`
- db_path: `database/brickovery.db`
- db_sha256: `db5cd41bf2b2b9baae5cee0fd63da224af8659174cebe72c6a267a3178728e2d`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260613_021313Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260613_021313Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "5286ac34f27773cde21beda08bc00fffaa32c69cf7178fb1a185a1dc0770a6fd",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260613_021313Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 206792,
    "items_db": 207329,
    "items_missing_in_db": 68,
    "codes_upstream": 84706,
    "codes_db": 249247,
    "codes_missing_in_db": 27,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "ad5f51cf54cae69dfdc837cadc3b79828a1a6be1f82f86554da223c09caa4675",
  "csv_size_bytes": 26377958,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260613_021313Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 206792,
  "items_db": 207329,
  "items_missing_in_db": 68,
  "codes_upstream": 84706,
  "codes_db": 249247,
  "codes_missing_in_db": 27,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 68,
  "db_inserted_codes": 25
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 249340,
  "distinct_bl_part_id": 172656,
  "null_boid": 171164,
  "null_weight": 94694,
  "null_bk_part_id": 93,
  "null_bk_part_key": 93,
  "null_api_item_type": 93,
  "null_brikick_name": 93,
  "null_part_name": 95619,
  "null_element_id": 166103,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171164`
- null_weight: `94694`
- corruption_pattern_count: `0`
