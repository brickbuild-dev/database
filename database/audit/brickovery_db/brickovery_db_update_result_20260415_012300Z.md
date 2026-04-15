# Brikick DB Post-Update Report

- created_at_utc: `20260415_012300Z`
- db_path: `database/brickovery.db`
- db_sha256: `288bec65693d49122a00723b1bf2e903b070eb1530e9846f7fa0c4d12eda7328`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260415_012248Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260415_012248Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "ef5cce1cd32e21f5ad111810c500b1ff08184406095047a719571080097f2c48",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260415_012248Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205201,
    "items_db": 205537,
    "items_missing_in_db": 12,
    "codes_upstream": 84156,
    "codes_db": 246049,
    "codes_missing_in_db": 7,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "e5538294f548585cb5c9b4fc911e4d862d23a2d38c115cf6f489e3a3a4dfc61f",
  "csv_size_bytes": 26192947,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260415_012248Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205201,
  "items_db": 205537,
  "items_missing_in_db": 12,
  "codes_upstream": 84156,
  "codes_db": 246049,
  "codes_missing_in_db": 7,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 12,
  "db_inserted_codes": 7
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246068,
  "distinct_bl_part_id": 171195,
  "null_boid": 167898,
  "null_weight": 92205,
  "null_bk_part_id": 19,
  "null_bk_part_key": 19,
  "null_api_item_type": 19,
  "null_brikick_name": 19,
  "null_part_name": 92347,
  "null_element_id": 162831,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167898`
- null_weight: `92205`
- corruption_pattern_count: `0`
