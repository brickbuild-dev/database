# Brikick DB Post-Update Report

- created_at_utc: `20260303_010756Z`
- db_path: `database/brickovery.db`
- db_sha256: `b499d2865112b6d69929c9b6f352cda62809821269018cb66606c6e83a3439f4`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260303_010745Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260303_010745Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "486209a02fb89e13d92605254830e962e61ce009be61e273b8d3d9056aaa2095",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260303_010745Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203277,
    "items_db": 203268,
    "items_missing_in_db": 58,
    "codes_upstream": 83757,
    "codes_db": 243393,
    "codes_missing_in_db": 31,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "7f7f8a95ee8a1d34a9ae74cb244de6bf6c752cbdd2cdc0dce251735daa679c2e",
  "csv_size_bytes": 26043053,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260303_010745Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203277,
  "items_db": 203268,
  "items_missing_in_db": 58,
  "codes_upstream": 83757,
  "codes_db": 243393,
  "codes_missing_in_db": 31,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 58,
  "db_inserted_codes": 31
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243482,
  "distinct_bl_part_id": 169042,
  "null_boid": 165315,
  "null_weight": 89694,
  "null_bk_part_id": 89,
  "null_bk_part_key": 89,
  "null_api_item_type": 89,
  "null_brikick_name": 89,
  "null_part_name": 89761,
  "null_element_id": 160245,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165315`
- null_weight: `89694`
- corruption_pattern_count: `0`
