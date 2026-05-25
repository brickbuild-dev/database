# Brikick DB Post-Update Report

- created_at_utc: `20260525_021402Z`
- db_path: `database/brickovery.db`
- db_sha256: `bd33d38b18bb15489b1d39a95ae226a0a6c468d0baf4717501b5e45b539b5e42`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260525_021350Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260525_021350Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "c4073cc0f2d52bb537a1c4f30ec47dae9856f7bed7c84bf0138e4a1f9ed46fa2",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260525_021350Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205931,
    "items_db": 206480,
    "items_missing_in_db": 13,
    "codes_upstream": 84409,
    "codes_db": 248153,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "c504f4435d986c8a915739de7e985ea972b0132c6d32229eb155e77dc6dd62bd",
  "csv_size_bytes": 26314346,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260525_021350Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205931,
  "items_db": 206480,
  "items_missing_in_db": 13,
  "codes_upstream": 84409,
  "codes_db": 248153,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 13,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248166,
  "distinct_bl_part_id": 172016,
  "null_boid": 169991,
  "null_weight": 93603,
  "null_bk_part_id": 13,
  "null_bk_part_key": 13,
  "null_api_item_type": 13,
  "null_brikick_name": 13,
  "null_part_name": 94445,
  "null_element_id": 164929,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169991`
- null_weight: `93603`
- corruption_pattern_count: `0`
