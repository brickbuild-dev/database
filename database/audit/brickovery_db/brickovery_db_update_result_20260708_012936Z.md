# Brikick DB Post-Update Report

- created_at_utc: `20260708_012936Z`
- db_path: `database/brickovery.db`
- db_sha256: `225f85dc4593a6f1b8f0ded93137df7ed2dc6303cd47c47e976e900333ae7629`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260708_012926Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260708_012926Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "3958b9917853815492cf784d1ed912597fc01bc8bd37578a70f91dc0d98ffd12",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260708_012926Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207753,
    "items_db": 208418,
    "items_missing_in_db": 13,
    "codes_upstream": 85226,
    "codes_db": 250871,
    "codes_missing_in_db": 12,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "b77323f73c532b04e2c8fda4f013872f9b856c7602b3973c0d5ff3fcbda6ff98",
  "csv_size_bytes": 26471253,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260708_012926Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207753,
  "items_db": 208418,
  "items_missing_in_db": 13,
  "codes_upstream": 85226,
  "codes_db": 250871,
  "codes_missing_in_db": 12,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 13,
  "db_inserted_codes": 9
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250893,
  "distinct_bl_part_id": 173651,
  "null_boid": 172717,
  "null_weight": 96167,
  "null_bk_part_id": 22,
  "null_bk_part_key": 22,
  "null_api_item_type": 22,
  "null_brikick_name": 22,
  "null_part_name": 97172,
  "null_element_id": 167656,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172717`
- null_weight: `96167`
- corruption_pattern_count: `0`
