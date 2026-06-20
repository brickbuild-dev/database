# Brikick DB Post-Update Report

- created_at_utc: `20260620_021309Z`
- db_path: `database/brickovery.db`
- db_sha256: `1a77caa955c8da68c71d170e1f6f807bb7ab5028eb1256e2fe44585b1712ec2a`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260620_021257Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260620_021257Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "fb670d0f1d11219108d1c48fe00816f9ea790a93d1bd8e33521418f83ccebb3a",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260620_021257Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207326,
    "items_db": 207896,
    "items_missing_in_db": 62,
    "codes_upstream": 84901,
    "codes_db": 250018,
    "codes_missing_in_db": 2,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "5b2b55dc9433b76584594f60576bad1e1a80d13427a5ef04fc57c0585d499271",
  "csv_size_bytes": 26421516,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260620_021257Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207326,
  "items_db": 207896,
  "items_missing_in_db": 62,
  "codes_upstream": 84901,
  "codes_db": 250018,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 62,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250082,
  "distinct_bl_part_id": 173213,
  "null_boid": 171906,
  "null_weight": 95416,
  "null_bk_part_id": 64,
  "null_bk_part_key": 64,
  "null_api_item_type": 64,
  "null_brikick_name": 64,
  "null_part_name": 96361,
  "null_element_id": 166845,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171906`
- null_weight: `95416`
- corruption_pattern_count: `0`
