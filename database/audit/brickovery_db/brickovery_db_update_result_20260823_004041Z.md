# Brikick DB Post-Update Report

- created_at_utc: `20260823_004041Z`
- db_path: `database/brickovery.db`
- db_sha256: `39d817a4aac59881e452eba5ef2cde73759a5c670c0589d25b853b8a54cd01e2`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260823_004029Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260823_004029Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "d279d60c3251305c3010619fb309cf75cb326015deb427bd8e71033ad1a6e87b",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260823_004029Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209779,
    "items_db": 210576,
    "items_missing_in_db": 1,
    "codes_upstream": 86304,
    "codes_db": 254130,
    "codes_missing_in_db": 5,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "19f192fdb54492c67507fbc10f7fb963d774d833f99f53e00696544e8ce01dbb",
  "csv_size_bytes": 26656494,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260823_004029Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209779,
  "items_db": 210576,
  "items_missing_in_db": 1,
  "codes_upstream": 86304,
  "codes_db": 254130,
  "codes_missing_in_db": 5,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 1,
  "db_inserted_codes": 5
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254136,
  "distinct_bl_part_id": 175621,
  "null_boid": 175959,
  "null_weight": 98937,
  "null_bk_part_id": 6,
  "null_bk_part_key": 6,
  "null_api_item_type": 6,
  "null_brikick_name": 6,
  "null_part_name": 100415,
  "null_element_id": 170899,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175959`
- null_weight: `98937`
- corruption_pattern_count: `0`
