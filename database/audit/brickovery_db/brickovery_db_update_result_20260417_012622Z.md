# Brikick DB Post-Update Report

- created_at_utc: `20260417_012622Z`
- db_path: `database/brickovery.db`
- db_sha256: `a71966a2c62745e857c342201db4e49d94133c29c824ac595c1c6785a22da300`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260417_012610Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260417_012610Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "c7a0e217cdc246ef731ae1074c33c44643a99ae1467c61b3f7d4199eba5d9964",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260417_012610Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205213,
    "items_db": 205553,
    "items_missing_in_db": 8,
    "codes_upstream": 84160,
    "codes_db": 246076,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "8c0715ce7ddc975b591ddb537f231b6d7874852aca1bc4c233eff75c2309f8b2",
  "csv_size_bytes": 26194542,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260417_012610Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205213,
  "items_db": 205553,
  "items_missing_in_db": 8,
  "codes_upstream": 84160,
  "codes_db": 246076,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 8,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246084,
  "distinct_bl_part_id": 171205,
  "null_boid": 167914,
  "null_weight": 92217,
  "null_bk_part_id": 8,
  "null_bk_part_key": 8,
  "null_api_item_type": 8,
  "null_brikick_name": 8,
  "null_part_name": 92363,
  "null_element_id": 162847,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167914`
- null_weight: `92217`
- corruption_pattern_count: `0`
