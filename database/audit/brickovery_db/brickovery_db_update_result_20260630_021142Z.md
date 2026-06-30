# Brikick DB Post-Update Report

- created_at_utc: `20260630_021142Z`
- db_path: `database/brickovery.db`
- db_sha256: `9794dc12b17bc4dc62ba16e15c22ee2810afc7bd18ce1d899480f411265ce6cf`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260630_021130Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260630_021130Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "a1a478d707d82fac2dc67bdcfa057b97ae8613a8e2b07a7c4af00d3d9f52d73d",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260630_021130Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207559,
    "items_db": 208221,
    "items_missing_in_db": 14,
    "codes_upstream": 85118,
    "codes_db": 250533,
    "codes_missing_in_db": 49,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "2ea10daf344c9b22d56a3dd3c89a4e1e9c846be5f2139dc866661ba7aaf48662",
  "csv_size_bytes": 26451620,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260630_021130Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207559,
  "items_db": 208221,
  "items_missing_in_db": 14,
  "codes_upstream": 85118,
  "codes_db": 250533,
  "codes_missing_in_db": 49,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 14,
  "db_inserted_codes": 48
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250595,
  "distinct_bl_part_id": 173482,
  "null_boid": 172419,
  "null_weight": 95912,
  "null_bk_part_id": 62,
  "null_bk_part_key": 62,
  "null_api_item_type": 62,
  "null_brikick_name": 62,
  "null_part_name": 96874,
  "null_element_id": 167358,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172419`
- null_weight: `95912`
- corruption_pattern_count: `0`
