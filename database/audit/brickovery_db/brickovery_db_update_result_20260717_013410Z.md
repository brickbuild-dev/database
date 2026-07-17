# Brikick DB Post-Update Report

- created_at_utc: `20260717_013410Z`
- db_path: `database/brickovery.db`
- db_sha256: `df491eec03c6f0decf81cac3ba32ae579da414a466119a8739196425b9a409e8`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260717_013400Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260717_013400Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "273d935b60b8b811cd545a7cd2d2b1d281fee17ec3291b72f038f61eaf919a7b",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260717_013400Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207877,
    "items_db": 208557,
    "items_missing_in_db": 13,
    "codes_upstream": 85367,
    "codes_db": 251159,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "11c24b0ca9f63a4f2d5014a4afb25db5b33117ccc50d7f0982ce75a017a446e0",
  "csv_size_bytes": 26487843,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260717_013400Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207877,
  "items_db": 208557,
  "items_missing_in_db": 13,
  "codes_upstream": 85367,
  "codes_db": 251159,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 13,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251173,
  "distinct_bl_part_id": 173790,
  "null_boid": 172997,
  "null_weight": 96344,
  "null_bk_part_id": 14,
  "null_bk_part_key": 14,
  "null_api_item_type": 14,
  "null_brikick_name": 14,
  "null_part_name": 97452,
  "null_element_id": 167936,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172997`
- null_weight: `96344`
- corruption_pattern_count: `0`
