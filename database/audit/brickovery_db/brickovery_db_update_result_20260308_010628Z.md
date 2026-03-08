# Brikick DB Post-Update Report

- created_at_utc: `20260308_010628Z`
- db_path: `database/brickovery.db`
- db_sha256: `231544762aac707f4cf530dda431482230e6c9f08c470f9aaae9b67977f6d390`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260308_010617Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260308_010617Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "1f8daa9f2867e724f98f4e32df889c179edd186b0dd95f20b0fb0d9bb3d69f8b",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260308_010617Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203390,
    "items_db": 203402,
    "items_missing_in_db": 43,
    "codes_upstream": 83862,
    "codes_db": 243628,
    "codes_missing_in_db": 29,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "df4cbe2236badfe7f9ee14a71bdc16a6ce3ea9f83116d86780ea30ef079d0622",
  "csv_size_bytes": 26056624,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260308_010617Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203390,
  "items_db": 203402,
  "items_missing_in_db": 43,
  "codes_upstream": 83862,
  "codes_db": 243628,
  "codes_missing_in_db": 29,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 43,
  "db_inserted_codes": 23
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243694,
  "distinct_bl_part_id": 169161,
  "null_boid": 165527,
  "null_weight": 89888,
  "null_bk_part_id": 66,
  "null_bk_part_key": 66,
  "null_api_item_type": 66,
  "null_brikick_name": 66,
  "null_part_name": 89973,
  "null_element_id": 160457,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165527`
- null_weight: `89888`
- corruption_pattern_count: `0`
