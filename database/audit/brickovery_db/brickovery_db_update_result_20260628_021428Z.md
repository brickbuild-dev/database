# Brikick DB Post-Update Report

- created_at_utc: `20260628_021428Z`
- db_path: `database/brickovery.db`
- db_sha256: `0e987ecfbd85a1c9207e1e86c5509710f8969917fcdae0b87dfb19195170a55d`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260628_021420Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260628_021420Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "b746b120675e2c61eb8589e1c51625f8a28bc68537352171ecee42bb05da4c6f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260628_021420Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207535,
    "items_db": 208203,
    "items_missing_in_db": 4,
    "codes_upstream": 85062,
    "codes_db": 250502,
    "codes_missing_in_db": 4,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "bca5bdd2ac3dbbbab3c61c6277e8ba938ade20238d037664803a06f742a5ddc8",
  "csv_size_bytes": 26449826,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260628_021420Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207535,
  "items_db": 208203,
  "items_missing_in_db": 4,
  "codes_upstream": 85062,
  "codes_db": 250502,
  "codes_missing_in_db": 4,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 4,
  "db_inserted_codes": 3
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250509,
  "distinct_bl_part_id": 173454,
  "null_boid": 172333,
  "null_weight": 95829,
  "null_bk_part_id": 7,
  "null_bk_part_key": 7,
  "null_api_item_type": 7,
  "null_brikick_name": 7,
  "null_part_name": 96788,
  "null_element_id": 167272,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172333`
- null_weight: `95829`
- corruption_pattern_count: `0`
