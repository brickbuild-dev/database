# Brikick DB Post-Update Report

- created_at_utc: `20260615_023934Z`
- db_path: `database/brickovery.db`
- db_sha256: `79ba871d13f82e608df91f3c171012f9f893d860848caf6e2dfd9c01d858c9f7`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260615_023924Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260615_023924Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "4474e3fc4ccac26460a6e273f07d19b5f68097ab29e1823f34d5a8056a99d02e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260615_023924Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207146,
    "items_db": 207661,
    "items_missing_in_db": 96,
    "codes_upstream": 84788,
    "codes_db": 249638,
    "codes_missing_in_db": 47,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "ef1874d32afbf29f3213f71f0a86ce6ec6e368db52b6d0d5e4cbc84ad92f27aa",
  "csv_size_bytes": 26399531,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260615_023924Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207146,
  "items_db": 207661,
  "items_missing_in_db": 96,
  "codes_upstream": 84788,
  "codes_db": 249638,
  "codes_missing_in_db": 47,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 96,
  "db_inserted_codes": 44
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 249778,
  "distinct_bl_part_id": 173016,
  "null_boid": 171602,
  "null_weight": 95122,
  "null_bk_part_id": 140,
  "null_bk_part_key": 140,
  "null_api_item_type": 140,
  "null_brikick_name": 140,
  "null_part_name": 96057,
  "null_element_id": 166541,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171602`
- null_weight: `95122`
- corruption_pattern_count: `0`
