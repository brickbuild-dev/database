# Brikick DB Post-Update Report

- created_at_utc: `20260324_010346Z`
- db_path: `database/brickovery.db`
- db_sha256: `5be2ae4392955bb064b09b4336fbe4a0cfda89063e809a536ee9380564db1567`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260324_010335Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260324_010335Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "4379ce502d6b978d1b74494021571e1eba083b5502846ec688795f69bc32243e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260324_010335Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203778,
    "items_db": 203867,
    "items_missing_in_db": 4,
    "codes_upstream": 84053,
    "codes_db": 244293,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "a163353e4da6fccfde20f17a9815e3e5fd4a05ec839992eaae6879590d52b67c",
  "csv_size_bytes": 26094491,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260324_010335Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203778,
  "items_db": 203867,
  "items_missing_in_db": 4,
  "codes_upstream": 84053,
  "codes_db": 244293,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 4,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 244298,
  "distinct_bl_part_id": 169573,
  "null_boid": 166130,
  "null_weight": 90460,
  "null_bk_part_id": 5,
  "null_bk_part_key": 5,
  "null_api_item_type": 5,
  "null_brikick_name": 5,
  "null_part_name": 90577,
  "null_element_id": 161061,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `166130`
- null_weight: `90460`
- corruption_pattern_count: `0`
